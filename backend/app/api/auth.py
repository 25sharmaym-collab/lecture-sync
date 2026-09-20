from datetime import timedelta
from fastapi import APIRouter,Depends,HTTPException,Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.core.config import get_settings
from app.core.db import get_db
from app.core.rate_limit import check_rate_limit
from app.core.security import hash_password
from app.models.user import User
from app.schemas.auth import *
from app.services.auth import authenticate,issue_auth_tokens,register
from app.services.email import send_email
from app.services.token import consume_token,issue_token,revoke_token
router=APIRouter(prefix='/auth',tags=['auth'])
@router.post('/register',response_model=UserResponse,status_code=201)
async def register_user(p:RegisterRequest,request:Request,db:AsyncSession=Depends(get_db)):
    await check_rate_limit(request,'register',5,3600)
    try:
        u=await register(db,p.email,p.password); s=get_settings(); t=await issue_token(db,u.id,'email_verification',timedelta(hours=s.verification_token_hours)); await db.commit(); await send_email(u.email,'Verify your LectureSync email',f'{s.frontend_url}/verify-email?token={t}'); return u
    except ValueError as e: await db.rollback(); raise HTTPException(409,str(e))
@router.post('/login',response_model=AuthResponse)
async def login(p:LoginRequest,request:Request,db:AsyncSession=Depends(get_db)):
    await check_rate_limit(request,'login',10,60); u=await authenticate(db,p.email,p.password)
    if not u: raise HTTPException(401,'Invalid email or password')
    a,r=await issue_auth_tokens(db,u); await db.commit(); return AuthResponse(access_token=a,refresh_token=r,user=u)
@router.post('/verify-email')
async def verify_email(p:VerifyEmailRequest,db:AsyncSession=Depends(get_db)):
    t=await consume_token(db,p.token,'email_verification')
    if not t: raise HTTPException(400,'Invalid or expired verification token')
    u=await db.get(User,t.user_id); u.is_email_verified=True; await revoke_token(db,p.token); await db.commit(); return {'message':'Email verified successfully'}
@router.post('/resend-verification')
async def resend(p:ResendVerificationRequest,request:Request,db:AsyncSession=Depends(get_db)):
    await check_rate_limit(request,'verify',10,60); u=await db.scalar(select(User).where(User.email==p.email.lower()))
    if u and not u.is_email_verified:
        s=get_settings(); t=await issue_token(db,u.id,'email_verification',timedelta(hours=s.verification_token_hours)); await db.commit(); await send_email(u.email,'Verify your LectureSync email',f'{s.frontend_url}/verify-email?token={t}')
    return {'message':'If the account exists and needs verification, an email has been sent'}
@router.post('/refresh',response_model=AuthResponse)
async def refresh(p:RefreshRequest,db:AsyncSession=Depends(get_db)):
    t=await consume_token(db,p.refresh_token,'refresh')
    if not t: raise HTTPException(401,'Invalid or expired refresh token')
    u=await db.get(User,t.user_id)
    if not u or not u.is_active: raise HTTPException(401,'User not found')
    await revoke_token(db,p.refresh_token); a,r=await issue_auth_tokens(db,u); await db.commit(); return AuthResponse(access_token=a,refresh_token=r,user=u)
@router.post('/logout')
async def logout(p:RefreshRequest,db:AsyncSession=Depends(get_db)):
    await revoke_token(db,p.refresh_token); await db.commit(); return {'message':'Logged out'}
@router.post('/forgot-password')
async def forgot(p:ForgotPasswordRequest,request:Request,db:AsyncSession=Depends(get_db)):
    await check_rate_limit(request,'forgot-password',5,3600); u=await db.scalar(select(User).where(User.email==p.email.lower()))
    if u:
        s=get_settings(); t=await issue_token(db,u.id,'password_reset',timedelta(hours=s.password_reset_hours)); await db.commit(); await send_email(u.email,'Reset your LectureSync password',f'{s.frontend_url}/reset-password?token={t}')
    return {'message':'If the account exists, a reset email has been sent'}
@router.post('/reset-password')
async def reset(p:ResetPasswordRequest,db:AsyncSession=Depends(get_db)):
    t=await consume_token(db,p.token,'password_reset')
    if not t: raise HTTPException(400,'Invalid or expired reset token')
    u=await db.get(User,t.user_id); u.password_hash=hash_password(p.new_password); await revoke_token(db,p.token); await db.commit(); return {'message':'Password reset successfully'}
@router.get('/me',response_model=UserResponse)
async def me(u:User=Depends(get_current_user)): return u

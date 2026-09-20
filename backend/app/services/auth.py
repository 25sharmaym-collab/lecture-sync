from datetime import timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import get_settings
from app.core.security import create_access_token,hash_password,verify_password
from app.models.user import User
from app.services.token import issue_token
async def register(db:AsyncSession,email:str,password:str)->User:
    if await db.scalar(select(User).where(User.email==email.lower())): raise ValueError('Email already registered')
    u=User(email=email.lower(),password_hash=hash_password(password)); db.add(u); await db.flush(); return u
async def authenticate(db:AsyncSession,email:str,password:str)->User|None:
    u=await db.scalar(select(User).where(User.email==email.lower()))
    return u if u and u.is_active and verify_password(password,u.password_hash) else None
async def issue_auth_tokens(db:AsyncSession,user:User)->tuple[str,str]:
    s=get_settings(); return create_access_token(str(user.id)),await issue_token(db,user.id,'refresh',timedelta(days=s.refresh_token_days))

from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.core.security import decode_access_token
from app.models.user import User
bearer=HTTPBearer(auto_error=False)
async def get_current_user(credentials:HTTPAuthorizationCredentials|None=Depends(bearer),db:AsyncSession=Depends(get_db))->User:
    if not credentials: raise HTTPException(401,'Authentication required')
    try:
        p=decode_access_token(credentials.credentials); uid=int(p['sub'])
        if p.get('type')!='access': raise ValueError
    except Exception: raise HTTPException(401,'Invalid or expired access token')
    u=await db.scalar(select(User).where(User.id==uid,User.is_active.is_(True)))
    if not u: raise HTTPException(401,'User not found')
    return u

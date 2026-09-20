from datetime import datetime,timedelta,timezone
import hashlib
from sqlalchemy import select,update
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_opaque_token
from app.models.token import Token
def hash_token(v:str)->str: return hashlib.sha256(v.encode()).hexdigest()
async def issue_token(db:AsyncSession,user_id:int,token_type:str,lifetime:timedelta)->str:
    raw=create_opaque_token(); db.add(Token(user_id=user_id,token_hash=hash_token(raw),token_type=token_type,expires_at=datetime.now(timezone.utc)+lifetime)); await db.flush(); return raw
async def consume_token(db:AsyncSession,raw:str,token_type:str)->Token|None:
    r=await db.execute(select(Token).where(Token.token_hash==hash_token(raw),Token.token_type==token_type)); t=r.scalar_one_or_none()
    if not t or t.revoked_at or t.expires_at<=datetime.now(timezone.utc): return None
    return t
async def revoke_token(db:AsyncSession,raw:str)->None:
    await db.execute(update(Token).where(Token.token_hash==hash_token(raw)).values(revoked_at=datetime.now(timezone.utc)))

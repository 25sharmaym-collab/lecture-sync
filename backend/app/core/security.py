from datetime import datetime, timedelta, timezone
import secrets
import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from app.core.config import get_settings
password_hasher=PasswordHasher()
def hash_password(password:str)->str: return password_hasher.hash(password)
def verify_password(password:str,password_hash:str)->bool:
    try: return password_hasher.verify(password_hash,password)
    except VerifyMismatchError: return False
def create_access_token(subject:str)->str:
    s=get_settings(); now=datetime.now(timezone.utc)
    return jwt.encode({'sub':subject,'type':'access','iat':now,'exp':now+timedelta(minutes=s.access_token_minutes)},s.secret_key,algorithm='HS256')
def create_opaque_token()->str: return secrets.token_urlsafe(48)
def decode_access_token(token:str)->dict: return jwt.decode(token,get_settings().secret_key,algorithms=['HS256'])

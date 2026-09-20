import time
from fastapi import HTTPException,Request,status
from redis.asyncio import Redis
from app.core.config import get_settings
redis_client=Redis.from_url(get_settings().redis_url,decode_responses=True)
async def check_rate_limit(request:Request,bucket:str,limit:int,window_seconds:int)->None:
    identity=request.client.host if request.client else 'unknown'; key=f'rl:{bucket}:{identity}:{int(time.time())//window_seconds}'
    count=await redis_client.incr(key)
    if count==1: await redis_client.expire(key,window_seconds)
    if count>limit: raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail='Rate limit exceeded')

import httpx
from app.core.config import get_settings
async def send_email(to_email:str,subject:str,body:str)->bool:
    s=get_settings()
    if not s.sendgrid_api_key: return False
    payload={'personalizations':[{'to':[{'email':to_email}]}],'from':{'email':s.sendgrid_from_email},'subject':subject,'content':[{'type':'text/plain','value':body}]}
    async with httpx.AsyncClient(timeout=10) as c:
        r=await c.post('https://api.sendgrid.com/v3/mail/send',headers={'Authorization':f'Bearer {s.sendgrid_api_key}','Content-Type':'application/json'},json=payload); r.raise_for_status()
    return True

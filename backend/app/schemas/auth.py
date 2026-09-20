from datetime import datetime
from pydantic import BaseModel,EmailStr,Field
class RegisterRequest(BaseModel): email:EmailStr; password:str=Field(min_length=8,max_length=128)
class LoginRequest(BaseModel): email:EmailStr; password:str
class UserResponse(BaseModel):
    id:int; email:EmailStr; is_active:bool; is_email_verified:bool; created_at:datetime
    model_config={'from_attributes':True}
class AuthResponse(BaseModel): access_token:str; refresh_token:str; token_type:str='bearer'; user:UserResponse
class RefreshRequest(BaseModel): refresh_token:str
class VerifyEmailRequest(BaseModel): token:str
class ResendVerificationRequest(BaseModel): email:EmailStr
class ForgotPasswordRequest(BaseModel): email:EmailStr
class ResetPasswordRequest(BaseModel): token:str; new_password:str=Field(min_length=8,max_length=128)

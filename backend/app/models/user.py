from datetime import datetime
from sqlalchemy import Boolean,DateTime,String,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.core.db import Base
class User(Base):
    __tablename__='users'; id:Mapped[int]=mapped_column(primary_key=True); email:Mapped[str]=mapped_column(String(320),unique=True,index=True); password_hash:Mapped[str]=mapped_column(String(512)); is_active:Mapped[bool]=mapped_column(Boolean,default=True,nullable=False); is_email_verified:Mapped[bool]=mapped_column(Boolean,default=False,nullable=False); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now()); updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    lectures=relationship('Lecture',back_populates='owner',cascade='all, delete-orphan'); tokens=relationship('Token',back_populates='user',cascade='all, delete-orphan')

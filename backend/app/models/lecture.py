from datetime import datetime
from sqlalchemy import Boolean,DateTime,ForeignKey,Integer,String,Text,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.core.db import Base
class Lecture(Base):
    __tablename__='lectures'; id:Mapped[int]=mapped_column(primary_key=True); owner_id:Mapped[int]=mapped_column(ForeignKey('users.id',ondelete='CASCADE'),index=True); title:Mapped[str]=mapped_column(String(255)); description:Mapped[str|None]=mapped_column(Text,nullable=True); video_path:Mapped[str|None]=mapped_column(String(1024),nullable=True); slides_path:Mapped[str|None]=mapped_column(String(1024),nullable=True); duration_seconds:Mapped[int|None]=mapped_column(Integer,nullable=True); is_public:Mapped[bool]=mapped_column(Boolean,default=False,nullable=False); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now()); updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    owner=relationship('User',back_populates='lectures')

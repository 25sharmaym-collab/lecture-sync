from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.core.db import get_db
from app.models.lecture import Lecture
from app.models.user import User
from app.schemas.lecture import LectureCreate,LectureResponse,LectureUpdate
router=APIRouter(prefix='/lectures',tags=['lectures'])
@router.post('',response_model=LectureResponse,status_code=201)
async def create(p:LectureCreate,u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    x=Lecture(owner_id=u.id,**p.model_dump()); db.add(x); await db.commit(); await db.refresh(x); return x
@router.get('',response_model=list[LectureResponse])
async def list_own(u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    r=await db.execute(select(Lecture).where(Lecture.owner_id==u.id).order_by(Lecture.created_at.desc())); return list(r.scalars())
@router.get('/public',response_model=list[LectureResponse])
async def public(db:AsyncSession=Depends(get_db)):
    r=await db.execute(select(Lecture).where(Lecture.is_public.is_(True)).order_by(Lecture.created_at.desc())); return list(r.scalars())
@router.get('/{lecture_id}',response_model=LectureResponse)
async def get(lecture_id:int,u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    x=await db.get(Lecture,lecture_id)
    if not x or (x.owner_id!=u.id and not x.is_public): raise HTTPException(404,'Lecture not found')
    return x
@router.put('/{lecture_id}',response_model=LectureResponse)
async def update(lecture_id:int,p:LectureUpdate,u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    x=await db.get(Lecture,lecture_id)
    if not x or x.owner_id!=u.id: raise HTTPException(404,'Lecture not found')
    for k,v in p.model_dump(exclude_unset=True).items(): setattr(x,k,v)
    await db.commit(); await db.refresh(x); return x
@router.delete('/{lecture_id}',status_code=204)
async def delete(lecture_id:int,u:User=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    x=await db.get(Lecture,lecture_id)
    if not x or x.owner_id!=u.id: raise HTTPException(404,'Lecture not found')
    await db.delete(x); await db.commit()

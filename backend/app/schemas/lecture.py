from datetime import datetime
from pydantic import BaseModel,Field
class LectureCreate(BaseModel): title:str=Field(min_length=1,max_length=255); description:str|None=None; is_public:bool=False
class LectureUpdate(BaseModel): title:str|None=Field(default=None,min_length=1,max_length=255); description:str|None=None; is_public:bool|None=None
class LectureResponse(BaseModel):
    id:int; owner_id:int; title:str; description:str|None; video_path:str|None; slides_path:str|None; duration_seconds:int|None; is_public:bool; created_at:datetime; updated_at:datetime
    model_config={'from_attributes':True}

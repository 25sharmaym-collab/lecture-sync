from pydantic import BaseModel
class TranscriptSegmentResponse(BaseModel):
    start:float
    end:float
    text:str
class TranscriptResponse(BaseModel):
    lecture_id:int
    segments:list[TranscriptSegmentResponse]
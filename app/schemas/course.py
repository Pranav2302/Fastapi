from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str  
    description: str

class CourseResponse(BaseModel):
    id: int
    title: str  
    description: str
    
    class Config:
        orm_mode = True
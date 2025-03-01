#here we are using pydantic model , which defines how should be request ,response be , we use it in parameter,pydantic is data validation
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class CourseResponse(CourseCreate):
    id: int
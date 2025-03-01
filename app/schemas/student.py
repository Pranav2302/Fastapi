#here we are using pydantic model , which defines how should be request,response be , we use it in parameter,pydantic is data validation
from pydantic import BaseModel

# Schema for creating a student (request validation)
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

# Schema for returning a student (response formatting)
class StudentResponse(StudentCreate):
    id: int  # Auto-add the ID to the response
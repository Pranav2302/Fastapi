from pydantic import BaseModel

# Schema for creating a student (request validation)
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

# Schema for returning a student (response formatting)
class StudentResponse(StudentCreate):
    id: int  # Auto-add the ID to the response
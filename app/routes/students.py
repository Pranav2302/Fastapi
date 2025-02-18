from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/students", dependencies=[Depends(get_current_user)])

@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    # Check for duplicate email
    existing = await db.execute(select(Student).filter(Student.email == student.email))
    if existing.scalar():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Save to database
    new_student = Student(**student.dict())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
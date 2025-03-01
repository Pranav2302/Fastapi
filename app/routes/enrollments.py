from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.enrollment import Enrollment
from app.models.student import Student
from app.models.course import Course
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/enrollments",tags=["enrollments"],dependencies=[Depends(get_current_user)])

@router.post("/")
async def enroll_student(student_id: int, course_id: int, db: AsyncSession = Depends(get_db)):
    # Check if student and course exist
    student = await db.get(Student, student_id)
    course = await db.get(Course, course_id)
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or course not found")
    
    # Create enrollment
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    await db.commit()
    return {"message": "Enrollment successful"}

@router.get("/students/{student_id}/courses")
async def get_enrolled_courses(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Fetch enrolled course IDs
    result = await db.execute(
        select(Course)
        .join(Enrollment)
        .filter(Enrollment.student_id == student_id)
    )
    courses = result.scalars().all()
    return {"enrolled_courses": courses}
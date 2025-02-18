from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseResponse
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=CourseResponse)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
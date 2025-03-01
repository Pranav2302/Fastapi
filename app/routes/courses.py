from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseResponse
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/courses",tags=["courses"],dependencies=[Depends(get_current_user)])

@router.post("/", response_model=CourseResponse) #reponse should be in courseresponse , defined in other file
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.dict()) # Create a new Course object
    db.add(new_course) # Add it to the session (pending commit)
    await db.commit() #  Commit transaction to save the course in the database
    await db.refresh(new_course) #Refresh the object with the latest DB state
    return new_course

@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
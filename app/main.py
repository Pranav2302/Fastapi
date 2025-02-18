from fastapi import FastAPI
from app.routes import students, auth, courses, enrollments

app = FastAPI(title="Student Management System")

# Include all routers
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Student Management System"}
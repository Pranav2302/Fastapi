from fastapi import FastAPI
from app.routes import students, auth, courses, enrollments
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Management System")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Student Management System , Go to API docs"}
            
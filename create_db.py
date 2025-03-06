import asyncio
import os
from app.database.database import Base, engine
from app.models.user import User
from app.models.student import Student
from app.models.course import Course
from app.models.enrollment import Enrollment
from app.routes.auth import get_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import SessionLocal

async def reset_database():
    # Delete database file
    if os.path.exists("students.db"):
        os.remove("students.db")
        print("Existing database deleted")
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Create admin user
    async with SessionLocal() as session:
        hashed_password = get_password_hash("secret")
        admin_user = User(username="admin", password=hashed_password,fullName="Administrator")
        session.add(admin_user)
        await session.commit()
        print("Admin user created")
    
    print("Database reset complete!")

if __name__ == "__main__":
    asyncio.run(reset_database())
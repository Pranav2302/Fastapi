from sqlalchemy import Column, Integer, String
from app.database.database import Base  # Fix the import path

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
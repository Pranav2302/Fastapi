from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base  # Fix the import path

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
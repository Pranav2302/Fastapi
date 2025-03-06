from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
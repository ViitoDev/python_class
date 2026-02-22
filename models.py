from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    profile = relationship("Profile", back_populates="Student", uselist=False, cascade="all, delete-orphan")

class Profile(Base):
    __tablename__ = "Profiles"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    adress = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    student = relationship("Student", back_populates="profile")
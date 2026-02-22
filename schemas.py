from typing import List, Optional
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    profile: Optional[profile] = None

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    name: str
    email: str
    profile: ProfileCreate

class Profile(BaseModel):
    id: int
    age: int
    adress: set

    class Confing:
        from_attribute = True

class ProfileCreate(BaseModel):
    age: int
    adress: str
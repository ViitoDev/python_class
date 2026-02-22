from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/students/', response_model=schemas.Student)
def student_create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(name = student.name, profile = models.profile(**student.profile.dict()))
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/students/', response_model=List[schemas.Student])
def students_list(db: Session = Depends(get_db)):
    students = db.query(models.Student).options(joinedload(models.Student.profile)).all()
    return students
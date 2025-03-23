from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from service import StudentService

app = FastAPI()
student_service = StudentService()


@app.get("/health")
def read_root():
    return {"health": "ok"}


# query student by id
@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student = student_service.get_student(student_id, db)
        return student.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/students")
def read_students(db: Session = Depends(get_db)):
    try:
        students = student_service.get_students(db)
        return [student.model_dump() for student in students]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

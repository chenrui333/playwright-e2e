from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from model import Student, StudentCreate
from service import StudentService

router = APIRouter(prefix="/students", tags=["students"])
student_service = StudentService()


@router.get("/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student = student_service.get_student(student_id, db)
        return student.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[Student])
def read_students(db: Session = Depends(get_db)):
    try:
        students = student_service.get_students(db)
        return [student.model_dump() for student in students]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Student)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    try:
        new_student = student_service.create_student(student_data.dict(), db)
        return new_student.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{student_id}", response_model=Student)
def update_student(
    student_id: int, student_data: StudentCreate, db: Session = Depends(get_db)
):
    try:
        updated_student = student_service.update_student(
            student_id, student_data.dict(), db
        )
        return updated_student.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student_service.delete_student(student_id, db)
        return {"detail": "Student deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import logging_config
from db import get_db
from model import Student, StudentCreate
from service import StudentService

logger = logging_config.get_logger(__name__)
router = APIRouter(prefix="/students", tags=["students"])
student_service = StudentService()


@router.get("/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)) -> Student:
    logger.info(f"Fetching student with ID: {student_id}")
    try:
        student = student_service.get_student(student_id, db)
        return student
    except ValueError as e:
        logger.error(f"Error fetching student with ID {student_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[Student])
def read_students(db: Session = Depends(get_db)) -> list[Student]:
    logger.info("Fetching all students")
    try:
        students = student_service.get_students(db)
        return [student for student in students]
    except ValueError as e:
        logger.error(f"Error fetching students: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Student)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)) -> Student:
    logger.info(f"Creating new student with data: {student_data}")
    try:
        new_student = student_service.create_student(student_data, db)
        return new_student
    except ValueError as e:
        logger.error(f"Error creating student: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{student_id}", response_model=Student)
def update_student(
    student_id: int, student_data: StudentCreate, db: Session = Depends(get_db)
) -> Student:
    logger.info(
        f"Updating student with ID: {student_id} with data: {student_data}"
    )
    try:
        updated_student = student_service.update_student(
            student_id, student_data, db
        )
        return updated_student
    except ValueError as e:
        logger.error(f"Error updating student with ID {student_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(
            f"Unexpected error updating student with ID {student_id}: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)) -> dict:
    logger.info(f"Deleting student with ID: {student_id}")
    try:
        student_service.delete_student(student_id, db)
        return {"detail": "Student deleted successfully"}
    except ValueError as e:
        logger.error(f"Error deleting student with ID {student_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(
            f"Unexpected error deleting student with ID {student_id}: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=str(e))

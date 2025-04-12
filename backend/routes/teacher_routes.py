from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service import teacher_service
from db import get_db

router = APIRouter(prefix="/teachers", tags=["teachers"])
service = teacher_service.TeacherService()

@router.get("/")
async def get_teachers(db: Session = Depends(get_db)):
    """
    Get a list of all teachers.
    """
    return service.get_all_teachers(db)

@router.get("/{teacher_id}")
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Get a teacher by ID.
    """
    print(teacher_id)
    return service.get_teacher_by_id(teacher_id, db)

@router.post("/")
async def create_teacher(teacher_data: dict, db: Session = Depends(get_db)):
    """
    Create a new teacher.
    """
    return service.create_teacher(teacher_data, db)

@router.put("/{teacher_id}")
async def update_teacher(teacher_id: int, teacher_data: dict, db: Session = Depends(get_db)):
    """
    Update an existing teacher.
    """
    return service.update_teacher(teacher_id, teacher_data, db)

@router.delete("/{teacher_id}")
async def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Delete a teacher by ID.
    """
    return service.delete_teacher(teacher_id, db)

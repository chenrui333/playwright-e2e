from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service import teacher_service
import logging_config
from db import get_db



router = APIRouter(prefix="/teachers", tags=["teachers"])
service = teacher_service.TeacherService()
logger = logging_config.get_logger(__name__)
@router.get("/")
async def get_teachers(db: Session = Depends(get_db)):
    logger.info("Fetching all teachers")
    """
    Get a list of all teachers.
    """
    return service.get_all_teachers(db)

@router.get("/{teacher_id}")
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Get a teacher by ID.
    """
    logger.info(f"Fetching teacher with ID: {teacher_id}")
    return service.get_teacher_by_id(teacher_id, db)

@router.post("/")
async def create_teacher(teacher_data: dict, db: Session = Depends(get_db)):
    """
    Create a new teacher.
    """
    logger.info("Creating a new teacher")
    return service.create_teacher(teacher_data, db)

@router.put("/{teacher_id}")
async def update_teacher(teacher_id: int, teacher_data: dict, db: Session = Depends(get_db)):
    """
    Update an existing teacher.
    """
    logger.info(f"Updating teacher with ID: {teacher_id}")
    return service.update_teacher(teacher_id, teacher_data, db)

@router.delete("/{teacher_id}")
async def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Delete a teacher by ID.
    """
    logger.info(f"Deleting teacher with ID: {teacher_id}")
    return service.delete_teacher(teacher_id, db)

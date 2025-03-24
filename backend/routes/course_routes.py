from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import logging_config
from db import get_db
from model import Course, CourseCreate
from service import CourseService

logger = logging_config.get_logger(__name__)
router = APIRouter(prefix="/courses", tags=["courses"])
course_service = CourseService()


@router.get("/{course_id}")
def read_course(course_id: int, db: Session = Depends(get_db)) -> Course:
    logger.info(f"Fetching course with ID: {course_id}")
    try:
        course = course_service.get_course(course_id, db)
        return course
    except ValueError as e:
        logger.error(f"Error fetching course with ID {course_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/")
def read_courses(db: Session = Depends(get_db)) -> list[Course]:
    logger.info("Fetching all courses")
    try:
        courses = course_service.get_courses(db)
        return [course for course in courses]
    except ValueError as e:
        logger.error(f"Error fetching courses: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/")
def create_course(course_data: CourseCreate, db: Session = Depends(get_db)) -> Course:
    logger.info(f"Creating new course with data: {course_data}")
    try:
        new_course = course_service.create_course(course_data, db)
        return new_course
    except ValueError as e:
        logger.error(f"Error creating course: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{course_id}")
def update_course(
    course_id: int, course_data: CourseCreate, db: Session = Depends(get_db)
) -> Course:
    logger.info(
        f"Updating course with ID: {course_id} with data: {course_data}"
    )
    try:
        updated_course = course_service.update_course(
            course_id, course_data, db
        )
        return updated_course
    except ValueError as e:
        logger.error(f"Error updating course with ID {course_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error while updating course: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)) -> dict:
    logger.info(f"Deleting course with ID: {course_id}")
    try:
        course_service.delete_course(course_id, db)
        return {"detail": f"Course with ID {course_id} deleted successfully"}
    except ValueError as e:
        logger.error(f"Error deleting course with ID {course_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error while deleting course: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

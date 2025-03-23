from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from model import Course, CourseCreate
from service import CourseService

router = APIRouter(prefix="/courses", tags=["courses"])
course_service = CourseService()


@router.get("/{course_id}", response_model=Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    try:
        course = course_service.get_course(course_id, db)
        return course.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[Course])
def read_courses(db: Session = Depends(get_db)):
    try:
        courses = course_service.get_courses(db)
        return [course.model_dump() for course in courses]
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Course)
def create_course(course_data: CourseCreate, db: Session = Depends(get_db)):
    try:
        new_course = course_service.create_course(course_data.dict(), db)
        return new_course.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{course_id}", response_model=Course)
def update_course(
    course_id: int, course_data: CourseCreate, db: Session = Depends(get_db)
):
    try:
        updated_course = course_service.update_course(course_id, course_data.dict(), db)
        return updated_course.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    try:
        course_service.delete_course(course_id, db)
        return {"detail": f"Course with ID {course_id} deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

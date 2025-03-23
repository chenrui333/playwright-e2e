from pydantic import BaseModel


class Course(BaseModel):
    course_id: int
    course_name: str
    credits: int
    department: str
    semester: str
    year: int


class CourseCreate(BaseModel):
    course_name: str
    credits: int
    department: str
    semester: str
    year: int

from pydantic import BaseModel

class Student(BaseModel):
    student_id: int
    name: str
    age: int
    enroll_year: int
    major: str
    gpa: float

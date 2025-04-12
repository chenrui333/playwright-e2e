from pydantic import BaseModel
from decimal import Decimal

class Teacher(BaseModel):
    """Base Teacher model with common attributes"""
    teacher_id: int
    first_name: str 
    last_name: str
    hire_year: int 
    department: str 
    salary: Decimal 

class TeacherCreate(BaseModel):
    """Teacher model for creation without ID"""
    first_name: str
    last_name: str 
    hire_year: int 
    department: str 
    salary: Decimal
from dao import StudentRepository
from model import Student

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()

    def get_student(self, student_id: int) -> Student:
        return self.student_repo.get_student_by_id(student_id)

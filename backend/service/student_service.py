from dao import StudentRepository
from model import Student

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()

    def get_student(self, student_id: int, db) -> Student:
        return self.student_repo.get_student_by_id(student_id, db)

    def get_students(self, db) -> list[Student]:
        return self.student_repo.get_all_students(db)

    def create_student(self, student_data: dict, db) -> Student:
        return self.student_repo.create_student(student_data, db)

    def update_student(self, student_id: int, student_data: dict, db) -> Student:
        return self.student_repo.update_student(student_id, student_data, db)

    def delete_student(self, student_id: int, db) -> None:
        return self.student_repo.delete_student(student_id, db)

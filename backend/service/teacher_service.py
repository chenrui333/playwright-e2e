from dao import TeacherRepository
from model import Teacher
class TeacherService:
    def __init__(self):
        self.teacher_repository = TeacherRepository()

    def get_teacher_by_id(self, teacher_id, db) -> Teacher:
        return self.teacher_repository.get_teacher_by_id(teacher_id, db=db)

    def get_all_teachers(self, db) -> list[Teacher]:
        return self.teacher_repository.get_all_teachers(db)

    def create_teacher(self, teacher_data, db) -> Teacher:
        return self.teacher_repository.create_teacher(teacher_data, db)

    def update_teacher(self, teacher_id, teacher_data, db) -> Teacher:
        return self.teacher_repository.update_teacher(teacher_id, teacher_data, db)

    def delete_teacher(self, teacher_id, db):
        return self.teacher_repository.delete_teacher(teacher_id, db)
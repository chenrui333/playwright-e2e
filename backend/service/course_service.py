from dao.course_repository import CourseRepository
from model.course import Course


class CourseService:
    def __init__(self):
        self.course_repo = CourseRepository()

    def get_course(self, course_id: int, db) -> Course:
        return self.course_repo.get_course_by_id(course_id, db)

    def get_courses(self, db) -> list[Course]:
        return self.course_repo.get_all_courses(db)

    def create_course(self, course_data: dict, db) -> Course:
        return self.course_repo.create_course(course_data, db)

    def update_course(self, course_id: int, course_data: dict, db) -> Course:
        return self.course_repo.update_course(course_id, course_data, db)

    def delete_course(self, course_id: int, db) -> None:
        return self.course_repo.delete_course(course_id, db)

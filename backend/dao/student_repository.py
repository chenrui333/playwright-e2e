from model import Student

class StudentRepository:
    def __init__(self):
        # TODO: sql connection setup
        pass

    def get_student_by_id(self, student_id: int) -> Student:
        # Simulated database query
        student_data = {
            "student_id": 1,
            "name": "John Doe",
            "age": 20,
            "enroll_year": 2021,
            "major": "Computer Science",
            "gpa": 3.8
        }

        # TOOD: student_data = db.query(Student).filter(Student.student_id == student_id).first()

        return Student(**student_data)

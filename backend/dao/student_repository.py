from sqlalchemy import text

from model import Student


class StudentRepository:
    def get_student_by_id(self, student_id: int, db) -> Student:
        SQL = text("""
            SELECT student_id, name, age, enroll_year, major, gpa
            FROM student
            WHERE student_id = :student_id
        """)
        result = db.execute(SQL, {"student_id": student_id})
        row = result.mappings().first()

        if not row:
            raise ValueError(f"Student with ID {student_id} not found")

        return Student(**row)

    def get_all_students(self, db) -> list[Student]:
        SQL = text("""
            SELECT student_id, name, age, enroll_year, major, gpa
            FROM student
        """)
        result = db.execute(SQL)
        rows = result.mappings().all()

        if not rows:
            return []

        students = [Student(**dict(row)) for row in rows]
        return students

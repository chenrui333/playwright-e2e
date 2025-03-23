import sqlite3
from model import Student

class StudentRepository:
    def __init__(self):
        self.conn = sqlite3.connect('coursework.db', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_student_by_id(self, student_id: int) -> Student:
        SQL = "SELECT student_id, name, age, enroll_year, major, gpa FROM student WHERE student_id = ?"
        self.cursor.execute(SQL, (student_id,))
        row = self.cursor.fetchone()

        if not row:
            raise ValueError(f"Student with ID {student_id} not found")

        student_data = dict(row)
        return Student(**student_data)

    def get_all_students(self) -> list[Student]:
        SQL = "SELECT student_id, name, age, enroll_year, major, gpa FROM student"
        self.cursor.execute(SQL)
        rows = self.cursor.fetchall()

        if not rows:
            return []

        students = [Student(**dict(row)) for row in rows]
        return students

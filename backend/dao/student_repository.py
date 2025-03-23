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

    def create_student(self, student_data: dict, db) -> Student:
        SQL = text("""
            INSERT INTO student (name, age, enroll_year, major, gpa)
            VALUES (:name, :age, :enroll_year, :major, :gpa)
        """)
        result = db.execute(SQL, student_data)
        db.commit()
        new_id = result.lastrowid

        if not new_id:
            raise ValueError("Failed to create student")
        return self.get_student_by_id(new_id, db)

    def update_student(self, student_id: int, student_data: dict, db) -> Student:
        SQL = text("""
            UPDATE student
            SET name = :name, age = :age, enroll_year = :enroll_year, major = :major, gpa = :gpa
            WHERE student_id = :student_id
        """)
        result = db.execute(SQL, {**student_data, "student_id": student_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Student with ID {student_id} not found")

        return self.get_student_by_id(student_id, db)

    def delete_student(self, student_id: int, db) -> None:
        SQL = text("""
            DELETE FROM student
            WHERE student_id = :student_id
        """)
        result = db.execute(SQL, {"student_id": student_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Student with ID {student_id} not found")

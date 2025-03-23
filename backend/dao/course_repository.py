from sqlalchemy import text

from model.course import Course


class CourseRepository:
    def get_course_by_id(self, course_id: int, db) -> Course:
        SQL = text("""
            SELECT course_id, course_name, credits, department, semester, year
            FROM course
            WHERE course_id = :course_id
        """)
        result = db.execute(SQL, {"course_id": course_id})
        row = result.mappings().first()

        if not row:
            raise ValueError(f"Course with ID {course_id} not found")

        return Course(**row)

    def get_all_courses(self, db) -> list[Course]:
        SQL = text("""
            SELECT course_id, course_name, credits, department, semester, year
            FROM course
        """)
        result = db.execute(SQL)
        rows = result.mappings().all()

        if not rows:
            return []

        courses = [Course(**row) for row in rows]
        return courses

    def create_course(self, course_data: dict, db) -> Course:
        SQL = text("""
            INSERT INTO course (course_name, credits, department, semester, year)
            VALUES (:course_name, :credits, :department, :semester, :year)
        """)
        result = db.execute(SQL, course_data)
        db.commit()
        new_id = result.lastrowid

        if not new_id:
            raise ValueError("Failed to create course")

        return self.get_course_by_id(new_id, db)

    def update_course(self, course_id: int, course_data: dict, db) -> Course:
        SQL = text("""
            UPDATE course
            SET course_name = :course_name,
                credits = :credits,
                department = :department,
                semester = :semester,
                year = :year
            WHERE course_id = :course_id
        """)
        result = db.execute(SQL, {**course_data, "course_id": course_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Course with ID {course_id} not found")

        return self.get_course_by_id(course_id, db)

    def delete_course(self, course_id: int, db) -> None:
        SQL = text("""
            DELETE FROM course
            WHERE course_id = :course_id
        """)
        result = db.execute(SQL, {"course_id": course_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Course with ID {course_id} not found")

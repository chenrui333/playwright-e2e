from sqlalchemy import text
from model import Teacher, TeacherCreate

class TeacherRepository:
    def get_teacher_by_id(self, teacher_id: str, db) -> Teacher | None:
        """
        Get a teacher by their ID.
        """
        SQL = text("""
            SELECT teacher_id, first_name, last_name, hire_year, department, salary FROM teacher
            WHERE teacher_id = :teacher_id
        """)
        result = db.execute(SQL, {"teacher_id": teacher_id})
        row = result.mappings().first()

        if not row:
            return None
        
        return Teacher(**row)
    

    def teacher_exist(self, first_name: str, last_name: str, db) -> bool:
        print(last_name + " " + first_name)
        """
        Get a teacher by their ID.
        """
        SQL = text("""
            SELECT EXISTS(SELECT teacher_id, first_name, last_name, hire_year, department, salary FROM teacher
            WHERE first_name = :first_name AND last_name = :last_name) AS teacher_exist
        """)
        result = db.execute(SQL, {"first_name": first_name, "last_name": last_name})
        exists = result.mappings().first().get("teacher_exist")

        return exists == 1
    
    def get_all_teachers(self, db) -> list[Teacher]:
        """
        Get all teachers.
        """
        SQL = text("""
            SELECT teacher_id, first_name, last_name, hire_year, department, salary 
            FROM teacher
        """)
        result = db.execute(SQL)
        rows = result.mappings().all()

        if not rows:
            return []
        
        teachers = [Teacher(**row) for row in rows]
        return teachers
    


    def create_teacher(self, teacher_data: dict, db) -> Teacher:
        isValidate = (self.teacher_exist(first_name=teacher_data.get("first_name"), last_name=teacher_data.get("last_name"), db=db))
        if isValidate:
            return ("Teacher already exists")
        

        # validate if teacher_data is actually data
        SQL = text("""
            INSERT INTO teacher (first_name, last_name, hire_year, department, salary)
            VALUES (:first_name, :last_name, :hire_year, :department, :salary)
        """)
        result = db.execute(SQL, teacher_data)
        db.commit()
        new_id = result.lastrowid

        if not new_id:
            raise ValueError("Failed to create teacher")
        return self.get_teacher_by_id(new_id, db) 

    def update_teacher(self, teacher_id: int, teacher_data: dict, db) -> Teacher:
        SQL = text("""
            UPDATE teacher
            SET first_name = :first_name, last_name = :last_name, hire_year = :hire_year, department = :department, salary = :salary
            WHERE teacher_id = :teacher_id
        """)
        result = db.execute(SQL, {**teacher_data, "teacher_id": teacher_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Teacher with ID {teacher_id} not found")

        return self.get_teacher_by_id(teacher_id, db)
    
    def delete_teacher(self, teacher_id: int, db) -> None:
        SQL = text("""
            DELETE FROM teacher
            WHERE teacher_id = :teacher_id
        """)
        result = db.execute(SQL, {"teacher_id": teacher_id})
        db.commit()

        if result.rowcount == 0:
            raise ValueError(f"Teacher with ID {teacher_id} not found")


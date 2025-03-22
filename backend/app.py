from fastapi import FastAPI
from service import StudentService

app = FastAPI()
student_service = StudentService()

@app.get("/")
def read_root():
    return {"health": "ok"}

# query student by id
@app.get("/students/{student_id}")
def read_student(student_id: int):
    student = student_service.get_student(student_id)
    return student.model_dump()

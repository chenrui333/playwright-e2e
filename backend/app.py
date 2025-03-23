from fastapi import FastAPI

from routes.course_routes import router as course_router
from routes.student_routes import router as student_router

app = FastAPI()

# include routes
app.include_router(course_router)
app.include_router(student_router)


@app.get("/health")
def read_root():
    return {"health": "ok"}

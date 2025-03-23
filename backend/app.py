from fastapi import FastAPI

import logging_config
from routes.course_routes import router as course_router
from routes.student_routes import router as student_router

logger = logging_config.get_logger(__name__)

app = FastAPI()

# include routes
app.include_router(course_router)
app.include_router(student_router)


@app.get("/health")
def read_root():
    logger.info("Health check endpoint called")
    return {"health": "ok"}

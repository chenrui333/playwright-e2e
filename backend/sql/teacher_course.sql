CREATE TABLE IF NOT EXISTS teacher_courses (
    teacher_id INTEGER,
    course_id INTEGER,
    semester TEXT NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE RESTRICT,
    PRIMARY KEY (teacher_id, course_id, semester, year)
);
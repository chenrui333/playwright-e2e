CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    enroll_year INTEGER NOT NULL,
    major TEXT NOT NULL,
    gpa REAL CHECK (gpa >= 0.0 AND gpa <= 4.0)
);

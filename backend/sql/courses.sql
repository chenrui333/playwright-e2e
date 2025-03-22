CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK (credits > 0),
    department TEXT NOT NULL,
    semester TEXT NOT NULL CHECK (semester IN ('Fall', 'Spring', 'Summer')),
    year INTEGER NOT NULL
);

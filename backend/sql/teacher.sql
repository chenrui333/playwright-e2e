CREATE TABLE IF NOT EXISTS teacher (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    hire_year INTEGER NOT NULL,
    department TEXT NOT NULL,
    salary REAL CHECK (salary >= 0.0)
);


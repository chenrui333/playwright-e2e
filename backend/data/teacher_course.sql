INSERT INTO teacher_courses (teacher_id, course_id, semester, year)
VALUES
    -- John Smith (CS Professor) teaches intro and data structures
    (1, 1, 'Fall', 2023),   -- Intro to Programming
    (1, 2, 'Spring', 2024), -- Data Structures
    
    -- Elizabeth Miller (CS Professor) teaches databases and OS
    (6, 3, 'Fall', 2024),    -- Database Systems
    (6, 4, 'Spring', 2025),  -- Operating Systems
    
    -- Both professors share advanced courses
    (1, 5, 'Fall', 2025),    -- Web Development
    (6, 6, 'Spring', 2026),  -- Machine Learning

    -- Cross-teaching to ensure coverage
    (6, 1, 'Spring', 2024),  -- Miller also teaches Intro
    (1, 3, 'Spring', 2024);  -- Smith also teaches Databases


-- Student grades manager

-- Drop tables if they already exist
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS grades;

-- 1.Сreate tables.
CREATE TABLE students
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Primary key
    full_name TEXT NOT NULL, -- Full name of the student
    birth_year INTEGER NOT NULL -- Year of birth
);

CREATE TABLE grades
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Primary key
    student_id INTEGER NOT NULL, -- Foreign key (references students.id)
    subject TEXT NOT NULL, -- Name of the subject
    grade INTEGER CHECK (grade BETWEEN 1 AND 100), -- Grade between 1 and 100
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- 2.Insert data.
INSERT INTO students(full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades(student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'Math', 89),
(9, 'English', 96),
(9, 'Art', 92);

-- 3.Find all grades for a specific student (Alice Johnson).
SELECT s.id, s.full_name, g.subject, g.grade
FROM students AS s
JOIN grades AS g ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4.Calculate the average grade per student.
SELECT s.full_name, ROUND(AVG(g.grade), 1) AS average_grade
FROM students AS s
JOIN grades AS g ON g.student_id = s.id
GROUP BY s.id, s.full_name;

-- 5.List all students born after 2004.
SELECT full_name, birth_year FROM students
WHERE birth_year > 2004;

-- 6.Create a query that lists all subjects and their average grades.
SELECT subject, ROUND(AVG(grade),1) AS average_grade
FROM grades
GROUP BY subject;

-- 7.Find the top 3 students with the highest average grades.
SELECT s.full_name, ROUND(AVG(g.grade), 1) AS average_grade
FROM students AS s
JOIN grades AS g ON g.student_id = s.id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 8.Show all students who have scored below 80 in any subject.
SELECT DISTINCT s.full_name
FROM students AS s
JOIN grades AS g ON g.student_id = s.id
WHERE g.grade < 80;
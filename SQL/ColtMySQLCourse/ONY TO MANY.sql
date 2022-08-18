CREATE TABLE students
(
	id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NOT NULL
);

CREATE TABLE papers
(
	title VARCHAR(255),
    grade decimal(4,2),
    student_id int,
    FOREIGN KEY(student_id) 
		REFERENCES students(id)
		ON DELETE CASCADE
);

INSERT INTO students (first_name) VALUES 
('Caleb'), 
('Samantha'), 
('Raj'), 
('Carlos'), 
('Lisa');
 
INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);

SELECT first_name, title, grade
FROM students JOIN papers 
	ON students.id = papers.student_id
ORDER BY grade DESC;

SELECT first_name, title, grade
FROM students LEFT JOIN papers 
	ON students.id = papers.student_id;
    
SELECT first_name, IFNULL(title, "Missing") as title, IFNULL(grade, 0) as grade
FROM students LEFT JOIN papers 
	ON students.id = papers.student_id;
    
SELECT first_name, IFNULL(AVG(grade), 0) as average
FROM students LEFT JOIN papers 
	ON students.id = papers.student_id
GROUP BY students.id
ORDER BY average DESC;

SELECT first_name, IFNULL(AVG(grade), 0) as average,
CASE 
	WHEN IFNULL(AVG(grade), 0)>75 THEN "PASSING"
    ELSE "FAILING"
END as "passing_status"
FROM students LEFT JOIN papers 
	ON students.id = papers.student_id
GROUP BY students.id
ORDER BY average DESC;
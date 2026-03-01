/*
INSERT INTO teachers (name, email)
VALUES('John Doe', 'john@codevalue.com');
INSERT INTO teachers (name, email)
VALUES('Dana Israeli', 'dana@codevalue.com')

SELECT * from teachers
*/
/*
INSERT INTO students (name, email)
VALUES('Micky Mouse', 'micky@mouse.com'),
	  ('Mini Mouse', 'mini@mouse.com')

SELECT * FROM students
*/
/*
INSERT INTO courses (name, teacher_id)
VALUES ('Advanced Python', 1), ('AI Workshop', 2)

SELECT * FROM courses
*/
/*
INSERT INTO students_to_courses(student_id, course_id, price_paid)
VALUES (1,1, 350.5), (1,2, 300), (2,1,600)
*/

/*
-- Show all courses per student
SELECT s.name, c.name FROM students s
JOIN students_to_courses stc ON stc.student_id = s.id
JOIN courses c ON c.id = stc.course_id
ORDER BY s.name, c.name

*/

/*
-- How much every student paid in total? (student name + total paid)
SELECT s.name, SUM(price_paid) FROM students s
JOIN students_to_courses stc ON stc.student_id = s.id
GROUP BY s.name
*/

/*
-- Average pay per student
SELECT s.name, AVG(price_paid) FROM students s
JOIN students_to_courses stc ON stc.student_id = s.id
GROUP BY s.name
*/

/*
-- Average pay per course
SELECT c.name, AVG(price_paid) FROM courses c
JOIN students_to_courses stc ON stc.course_id = c.id
GROUP BY c.name

*/




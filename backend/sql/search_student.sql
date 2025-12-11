/*
* Checks if a student exists in students table. Returns True/False
*/

SELECT EXISTS (
    SELECT 1 FROM students
    WHERE student_id = ? OR last_name = ?
);
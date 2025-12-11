/*
 * Checks if a tutor exists in tutors table. Returns True/False as ints
 */

SELECT EXISTS (
    SELECT 1 FROM tutors
    WHERE tutor_last_name = ?
);
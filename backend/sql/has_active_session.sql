/*
 * Confirm if student has an active session
 */

SELECT EXISTS(
    SELECT 1 FROM sessions
    WHERE student_id = ? AND active = 1
);
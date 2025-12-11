/*
 * Inserts a session into sessions table (Partial).
 */

 INSERT INTO sessions(student_id, active, tutor_last_name, start_time, end_time)
 VALUES              (?, 1, ?, CURRENT_TIMESTAMP, NULL);


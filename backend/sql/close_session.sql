/*
 * Updates the active and end_timestamp column (closes a session).
   it doesn't return the rows themselves, but it reports how many rows were affected.
 */

 UPDATE sessions
 SET active = 0, end_time = CURRENT_TIMESTAMP
 WHERE student_id = ? AND end_time is NULL AND active = 1;
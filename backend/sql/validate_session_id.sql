/*
 * Determines if a session_id expired
 */

SELECT CASE  WHEN expires_at < datetime('now') THEN 1 ELSE 0 END AS has_expired
FROM sessions 
WHERE session_id = ?;
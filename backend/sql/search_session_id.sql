/*
 * Searches for a session_id token
 */

SELECT EXISTS(
    SELECT 1 FROM sessions
    WHERE session_id = ?
);
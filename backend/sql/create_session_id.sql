/*
 * Creates a session_id
 */

INSERT INTO sessions (session_id, user_id, expires_at)
VALUES               (?, ?, datetime('now', '+60 minutes'));
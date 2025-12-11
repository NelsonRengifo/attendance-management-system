/*
 * Retrieves password_hash from users
 */

 SELECT password_hash FROM users WHERE username = ?;
/*
 * Inserts super admin into users table
 */ 


INSERT INTO users (username, password_hash, phone, email, is_active, user_role, first_name, last_name)
VALUES            (?, ?, ?, ?, 1, 'super_admin', ?, ?);
/*
 * Checks if a super admin exists.
 */

SELECT EXISTS(
    SELECT 1 FROM users WHERE user_role = 'super_admin' LIMIT 1
);

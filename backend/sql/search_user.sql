/*
 *  Checks if username exists
 */ 


 SELECT EXISTS (
    SELECT 1 FROM users 
    WHERE username = ?
 );
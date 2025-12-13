/*
 * Create Tables
 */

--  FRONTEND OF TUTOR & ADMIN -- 
--  Role	      UI Features Visible
--  Admin	      Create tutor, view stats, manage users, reports, view students, active sessions.
--  Tutor	      View/Retrieve student info, view active sessions, submit sessions, when they sign in, they check in.

 CREATE TABLE IF NOT EXISTS students (
   student_id INTEGER PRIMARY KEY, 
   first_name TEXT NOT NULL, 
   last_name TEXT NOT NULL, 
   major TEXT NOT NULL, 
   email TEXT NOT NULL
 );

 CREATE TABLE IF NOT EXISTS tutoring_sessions (
   session_id INTEGER PRIMARY KEY AUTOINCREMENT, 
   student_id INTEGER NOT NULL,
   active INTEGER NOT NULL, 
   tutor_last_name TEXT NOT NULL,  
   start_time TIMESTAMP NOT NULL, 
   end_time TIMESTAMP, 
   FOREIGN KEY (student_id) REFERENCES students (student_id)
 );

 CREATE TABLE IF NOT EXISTS tutors (
   tutor_id INTEGER PRIMARY KEY, 
   tutor_last_name TEXT NOT NULL, 
   tutor_first_name TEXT NOT NULL,
   subject_area TEXT NOT NULL, 
   major TEXT NOT NULL, 
   available INTEGER NOT NULL DEFAULT 0    -- REPRESENTS IF TUTOR IS PRESENT OR NOT. 0 = NO, 1 = YES. UPDATED BY TUTOR WHEN THEY CHECK IN
 );
 
-- Table for login credentials
CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  username INTEGER NOT NULL UNIQUE,               -- tutor school id or admin school id
  password_hash TEXT NOT NULL,
  phone TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  is_active INTEGER NOT NULL DEFAULT 0,        -- 0 NOT ACTIVE. 1 ACTIVE
  user_role TEXT NOT NULL,                     -- ADMIN OR TUTOR OR SUPER ADMIN
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      
);

-- keep track of the token lifetime once tutor receives email to change password
CREATE TABLE IF NOT EXISTS invite_tokens (
  token TEXT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  expires_at TIMESTAMP NOT NULL,            -- issued_at + 24hrs
  is_used INTEGER NOT NULL DEFAULT 0,       -- 0 = false, 1 = true
  issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users (user_id)  
);



CREATE TABLE IF NOT EXISTS sessions (
  session_id TEXT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);

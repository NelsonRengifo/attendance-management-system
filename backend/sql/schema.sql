/*
 * Create Tables
 */

--  FRONTEND OF TUTOR & ADMIN -- 
--  Role	      UI Features Visible
--  Admin	      Create tutor, view stats, manage users, reports, view students, active sessions.
--  Tutor	      View/retrieve student info, active sessions, submit sessions, checkin

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
   available INTEGER NOT NULL DEFAULT 0    -- REPRESENTS IF TUTOR IS PRESENT OR NOT. 0 = NO, 1 = YES. UPDATED BY TUTOR
 );
 
-- Table for login credentials
CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  phone TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  is_active INTEGER NOT NULL DEFAULT 0,   -- 0 NOT ACTIVE. UPDATE TO 1 ONCE TUTOR ACTIVATES ACCOUNT
  role TEXT NOT NULL,                     -- ADMIN OR TUTOR
  tutor_id INTEGER NOT NULL DEFAULT NULL  -- if role tutor, set this to the tutor id of tutors. users.tutor_id = tutors.tutor_id
  invited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT NULL,      -- UPDATE once Tutor accepts invite + sets password
  FOREIGN KEY (tutor_id) REFERENCES tutors (tutor_id)
);

-- keep track of the token lifetime once tutor receives email
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

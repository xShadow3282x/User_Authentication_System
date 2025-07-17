# User_Authentication_System

* Goal: Build a REST API where users can:

1. Register with username/email/password

2. Login and receive JWT token

3. Access protected routes using the token

 * Project Features
 
🔹 1. User Registration
Accepts username, email, and password

Validates input using Pydantic

Stores user in fake in-memory DB (dict)

Hashes passwords securely using bcrypt

🔹 2. User Login
Accepts username and password

Verifies credentials

Issues JWT access token valid for 30 minutes

🔹 3. Protected Route (/me)
Requires valid JWT token

Returns current user info (username, email)
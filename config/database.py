import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./config/connect.sqlite3')

    def register_users(self, user_details):
        cursor = self.conn.cursor()
        query = "INSERT INTO users (username, password, email) VALUES (?,?,?)"
        if cursor.execute(query, user_details):
            self.conn.commit()
            self.conn.close()
            return "User Registered"
        else:
            self.conn.close()
            return "Failed to register user"

    def login(self, login_details):
        cursor = self.conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        if cursor.execute(query, login_details):
            details = cursor.fetchall()
            if len(details) == 0:
                self.conn.close()
                return "Invalid username or password"
            else:
                self.conn.close()
                return "Login Successful"





import sqlite3

# db creation and adding a user table to it
connection = sqlite3.connect("C:/Users/rsisl/Learning/PythonWorkspace/Project/users.db", timeout=10)

cursor = connection.cursor()

#cursor.execute("DROP TABLE IF EXISTS user_info")

#cursor.execute("CREATE TABLE IF NOT EXISTS user_info (user_id INTEGER PRIMARY KEY, user_name TEXT NOT NULL, user_role TEXT NOT NULL, user_password TEXT NOT NULL)")

cursor.execute("INSERT INTO user_info SET user_name = 'Ashra' WHERE user_id = 8")

connection.close()
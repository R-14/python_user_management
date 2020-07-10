import sqlite3
from sqlite3 import OperationalError

# db creation and adding a user table to it
connection = sqlite3.connect("C:/Users/rsisl/Learning/PythonWorkspace/Project/users.db")

cursor = connection.cursor()


try:
    cursor = connection.cursor()
    #cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Jill Goodacre", "HR Assistant", "j£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Will Goodacre", "Department Manager", "w£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Bill Goodacre", "Assistant Manager", "b£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Till Goodacre", "Developer", "t£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Quill Goodacre", "Team Manager", "qu£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Nill Goodacre", "Tester", "n£$FGH%")''')
    cursor.execute(''' INSERT INTO user_info (user_name, user_role, user_password) VALUES ("Shill Goodacre", "Project Manager", "sh£$FGH%")''')
    connection.commit()
    print ("one record added successfully")
except OperationalError as errMsg:
    print(errMsg)
except:
    print ("error on INSERT")
    connection.rollback()
else:
    print("Success, no error!")
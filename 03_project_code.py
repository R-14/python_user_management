import sqlite3
from _sqlite3 import OperationalError

#connection = sqlite3.connect("users.db")
connection = sqlite3.connect("C:/Users/rsisl/Learning/PythonWorkspace/Project/users.db")

#open connection
cursor = connection.cursor()









# function to retrieve all users
def getUsers():    
    
   #declare rows so you can print out the items later    
    rows = ()
    
    try:        
        rows = connection.execute(
            "SELECT * FROM user_info;").fetchall()              

        for row in rows:
            print(row[0],row[1],row[2])
      
    except OperationalError as errMsg:
            print(errMsg)
    except:
            print ("error on Fetch")
            connection.rollback()
    finally:
            connection.close()
            print(row[0],row[1],row[2])              









#function to add one user
def addOneUser(userSelection):    
    
    #take input from the user and add to the sql db/table       
    user_input_name = input("Full Name: ")   
    user_input_role = input("Role : ")
    user_input_password = input("password : ")     
        
    #sql script to insert input data into user_info table    
    try:
        connection.execute(
            """INSERT INTO user_info(user_name, user_role, user_password) VALUES (?,?,?)""", 
            (user_input_name, user_input_role, user_input_password))
        connection.commit()
        print("one record added successfully") 
        
    except:
        print("error on INSERT")
        connection.rollback()
        
    finally:
        connection.close()



        









#function to delete one user from the db
def deleteOneUser(find_user_id):    
    """User record will delete row by id"""  
    rows = ()      
    try:            
        cursor.execute("DELETE FROM user_info WHERE user_id = ?", (find_user_id,))
        connection.commit()
        print ("User for:",  find_user_id, " has been deleted successfully")
    
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print ("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()
        return rows









#function for the menu
def welcomeMenu():
    print("Welcome to FDM's User Management System.")  
    #print("Please enter your login details")  
    #print(user_number)
    #print(user_pword)  
  
    #check for different users
    print("""Options:
          1. List users
          2. Add a new user
          3. Modify a user
          4. Delete one user
          5. Exit the system""")    
    
    try:
        #add more options
        Option = int(input("Please select one of the options from the menu: "))     
            
        #check the input
        if (Option == 1):
            print("List all users: ")
            print("\n", getUsers())
        elif (Option == 2):
            print("Please add a new user: ")
            print("\n", addOneUser(Option))
        elif (Option == 3):
            print("Please select which user's details you wish to amend: ")
            old_name = input("Please enter user name: ")
            find_id = input("Please input id of user : ")
            print("\n", updateOneUser(old_name, find_id)) 
        elif (Option == 4):
            person_you_want_to_delete = int(input("Please enter id of user you want to delete : "))
            print("\n", deleteOneUser(person_you_want_to_delete))
        elif (Option == 5):
            print("Goodbye.")            
        else :
            print("Please input a valid option : ") 
        
        return Option           
    
    except ValueError:
        print("Enter an integer value between 1 and 5")
        print("""Options:
          1. List users
          2. Add a new user
          3. Modify a user
          4. Delete user
          5. Exit the system""")
        Option = int(input("Please select one of the options from the menu: ")) 
        
def initializer():
    exit_now = 0
    while exit_now < 5:
        userSelection = welcomeMenu()  
        
        if userSelection == 5:
              exit_now = userSelection


initializer()
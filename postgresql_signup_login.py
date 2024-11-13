import psycopg2
import time



con = psycopg2.connect(
host = "localhost",
database = "postgres",
user = "postgres",
password = "postgres")
cursor = con.cursor()
   
def insert_info(name, password,reg_date):
    cursor.execute('''CREATE TABLE IF NOT EXISTS userdatabase(
                   id SERIAL PRIMARY KEY,
                   name TEXT,
                   password TEXT,
                   registration_date TEXT)''')
    
    cursor.execute('''INSERT INTO userdatabase (name, password, registration_date)
                   VALUES (%s, %s, %s)''',(name, password, reg_date))
    con.commit()

def signup():
    print("*****SIGN UP*****")
    bool = True
    user_list = []
    while bool:
        name = input("Name: ")

        # Test names
        cursor.execute('''SELECT name FROM userdatabase''')
        db_names = cursor.fetchall()
        # Append all names to list
        for db_name in db_names:
            user_list.append(db_name[0])
        if name.lower() in user_list:
                print("This name already taken")
        
        else:
            password = input("Password: ")
            while bool:
                password_again = input('Password again: ')
                if password == password_again:
                    #Registration time
                    reg_date = time.strftime("%Y-%m-%d %H:%M", time.localtime())
                    #Insert data to postgre database
                    insert_info(name.lower(), password, reg_date)

                    print("  Registration successful...")
                    bool = False
                else:
                    print("  Type the password correctly")
    


def login():
    print("*****LOGIN*****")
    print("  Close program type (0)")
    np_database ={}
    while True:
        name = input("Name: ")
        if name == "0":
            print("  Program closed...")
            break
        password = input("Password: ")

        cursor.execute('''SELECT name, password FROM userdatabase''')
        n_and_p = cursor.fetchall()
        for info in n_and_p:
            np_database[info[0]] = info[1]
        try:
            if np_database[name] == password:
                print("  Successful login...")
                break
        except KeyError:
            print("  Name or password incorrect")
                
            
while True:
    print('''WELCOME TO SIGNUP LOGIN PROGRAM''')
    print(''' ENTER (S) OR (0) FOR SIGNUP\n ENTER (L) OR (1) FOR LOGIN ''' )
    choice = input("Choice: ")
    if not choice:
        print("  Please enter choice")
    elif choice.upper() == "S" or choice == "0":
            signup()
    elif choice.upper() == "L" or choice == "1":
            login()
    else:
        print("  Please enter (S)(0)(L)(1) ")
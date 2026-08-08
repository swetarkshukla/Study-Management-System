import dashboard
def get_non_empty_data(prompt):
    while True:
        a=input(prompt).strip()
        if a == '':
            print("This field cannot be empty!")
        else:
            return a
def register():
    import sqlite3
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    while True:
        us_name=get_non_empty_data("Choose a username: ")
        cursor.execute("""SELECT * FROM Users WHERE Username = ?""",(us_name,))
        username_exist = cursor.fetchone()
        if username_exist:
            print("The username already exists, please try again!!")
        else:
            break
    while True:
        pas=input("Choose a password: ")
        if len(pas)>=8:
            break
        print("The password you entered is less than 8 characters. Please Try again!")
    cou=get_non_empty_data("Enter your course: ")
    n=get_non_empty_data("Enter your name: ")
    while True:
        try:
            sem=int(input("Enter your semester: "))
            if 1<=sem<=8:
                break
            else:
                print("Semester cant be greater then 8 or less then 1!")
        except ValueError:
            print("Invalid DataType for Semester!")
    while True:
        try:
            cg=float(input("Enter your target CGPA: "))
            if 0.0<=cg<=10.0:
                break
            else:
                 print("CGPA can't be bigger then 10.0 and less then 0.0!")
        except ValueError:
            print("Invalid DataType for CGPA!")
    cursor.execute("""INSERT INTO Users(Username, Password, Name, Course, Semester, Target_CGPA) VALUES(?,?,?,?,?,?)""",(us_name,pas,n,cou,sem,cg))
    conn.commit()
    conn.close()
    print('''✅ Registration Successful!
Please login to continue.''')
password_limit=0
def login():
    import sqlite3
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()
    global password_limit
    global user_id
    while(password_limit<3):
        k=False
        n=input("Enter your username: ")
        pa=input("Enter your password: ")
        cursor.execute("""SELECT * FROM Users WHERE Username =? AND Password=?""", (n,pa))
        check_username= cursor.fetchone()
        if check_username:
            user_id, username, password, name, course, semester, cgpa = check_username
            print("======================================")
            print("Welcome Back",name,"🔥")
            print("Course: ",course)
            print("Semester: ",semester)
            print("Target CGPA: ",cgpa, "💪")
            print("======================================")
            conn.close()
            k=True
            dashboard.second_landing_screen()
            break
        if k!=True:
            print("Username or password is incorrect.")
            password_limit+=1
        else:
            password_limit=0
            break
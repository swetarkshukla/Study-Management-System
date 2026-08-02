import database
import dashboard
import storage
def get_non_empty_data(prompt):
    while True:
        a=input(prompt).strip()
        if a == '':
            print("This field cannot be empty!")
        else:
            return a
def register():
    while True:
        us_name=get_non_empty_data("Choose a username: ")
        username_exist=False
        for ele in database.username:
            if ele==us_name:
                username_exist=True
                break
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
                database.semester.append(sem)
                break
            else:
                print("Semester cant be greater then 8 or less then 1!")
        except ValueError:
            print("Invalid DataType for Semester!")
    while True:
        try:
            cg=float(input("Enter your target CGPA: "))
            if 0.0<=cg<=10.0:
                database.cgpa_target.append(cg)
                break
            else:
                 print("CGPA can't be bigger then 10.0 and less then 0.0!")
        except ValueError:
            print("Invalid DataType for CGPA!")
    database.username.append(us_name)
    database.name.append(n)
    database.course.append(cou)
    database.password.append(pas)
    database.subject_uni.append([])
    database.tasks_uni.append([])
    storage.save_data()
    print('''✅ Registration Successful!
Please login to continue.''')
password_limit=0
def login():
    global password_limit
    while(password_limit<3):
        k=False
        n=input("Enter your username: ")
        pa=input("Enter your password: ")
        for i in range(0,len(database.username)):
            if database.username[i]==n and database.password[i]==pa:
                global usercode
                usercode=i
                print("======================================")
                print("Welcome Back",database.name[i],"🔥")
                print("Course: ",database.course[i])
                print("Semester: ",database.semester[i])
                print("Target CGPA: ",database.cgpa_target[i], "💪")
                print("======================================")
                k=True
                dashboard.second_landing_screen()
                break
        if k!=True:
            print("Username or password is incorrect.")
            password_limit+=1
        else:
            password_limit=0
            break

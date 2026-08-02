import subject
import task
import auth
import progress
def start():
    while True:
        print('''==============================================
                STUDY MANAGEMENT SYSTEM
==============================================
1.Register
2.Login
3.Exit''')
        try:
            ch=int(input("Enter 1,2 or 3 for your preferred action: "))
            if ch==1:
                auth.register()
            elif ch==2:
                auth.login()
                if auth.password_limit>=3:
                    print("Too many failed attempts! Try again")
                    auth.password_limit=0
                    return
            elif ch==3:
                print("Thank you for using STUDY MANAGEMENT SYSTEM")
                return
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid DataType for choice! Try again")
def second_landing_screen():
    while True:
        print('''==============================================
                DASHBOARD
==============================================
1.Subjects
2.Tasks
3.Progress
4.Return to Main Menu''')
        try:
            choice_dashboard=int(input("Enter your choice: "))
            if choice_dashboard==1:
                subject.subjects()
            elif choice_dashboard==2:
                task.tasks()
            elif choice_dashboard==3:
                progress.progress()
            elif choice_dashboard==4:
                return
        except ValueError:
            print("Invalid DataType for choice! Try again")
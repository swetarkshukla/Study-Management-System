import auth
import sqlite3
def tasks():
    while True:
        print('''==============================================
                TASKS
==============================================
1.Add Tasks
2.View Taks
3.Mark Task Completed
4.Delete Task
5.Back''')
        conn=sqlite3.connect("study.db")
        cursor=conn.cursor()
        while True:
            try:
                choice_tasks_menu=int(input("Enter your choice: "))
                if choice_tasks_menu==1:
                    while True:
                        try:
                            cursor.execute("""SELECT * FROM Subjects WHERE User_Id=?""",(auth.user_id,))
                            subjects=cursor.fetchall()
                            if subjects:
                                task=input("Enter your task: ")
                                a=1
                                for ele in subjects:
                                    print(a,ele[1])
                                    a+=1
                                k=int(input("Whats the task subject? "))
                                subje=subjects[k-1][1]
                                cursor.execute("""INSERT INTO Tasks(User_ID, Subject, Task, Completed) VALUES(?,?,?,?)""",(auth.user_id, subje, task,0))
                                conn.commit()
                                print("Task Added Sucessfully!")
                                break
                            else:
                                print("Add subjects first to write tasks!")
                        except IndexError:
                            print("Invalid choice for serial number!Try again")
                elif choice_tasks_menu==2:
                    print("=============YOUR TASKS================")
                    cursor.execute("SELECT * FROM Tasks WHERE User_ID=?",(auth.user_id,))
                    taskss=cursor.fetchall()
                    if taskss:
                        for ele in taskss:
                            if ele[4]:
                                print("✅", ele[3],"\nSubject: ",ele[2])
                            else:
                                print("❌", ele[3],"\nSubject: ",ele[2])
                    else:
                        print("No tasks added yet!")
                elif choice_tasks_menu==3:
                    cursor.execute("""SELECT * FROM Tasks WHERE User_ID=?""",(auth.user_id,))
                    taskss=cursor.fetchall()
                    print(taskss)
                    a=1
                    unfinished=[]
                    if taskss:
                        for ele in taskss:
                            if ele[4]==0:
                                print("Following are the unfinished tasks: ",a,ele[3])
                                unfinished.append(ele)
                                a+=1
                        while True:
                            try:
                                z=int(input("Enter the task you want to mark complete: "))
                                cursor.execute("""UPDATE Tasks SET Completed = 1 WHERE Task_ID=?""",(unfinished[z-1][0],))
                                print("✅Task mark completed successfully!")
                                conn.commit()
                                break
                            except ValueError:
                                print("Invalid DataType")
                            except IndexError:
                                print("Please enter the correct task number!")
                    else:
                        print("No task added yet!")
                elif choice_tasks_menu==4:
                    cursor.execute("""SELECT * FROM Tasks WHERE User_ID=?""",(auth.user_id,))
                    t=cursor.fetchall()
                    if t:
                        print("These are the current tasks.")
                        a=1
                        for ele in t:
                            print(a,ele[3])
                            a+=1
                        while True:
                            try:
                                l=int(input("Enter the serial no. of the task you want to delete: "))
                                cursor.execute("""DELETE FROM Tasks WHERE Task_ID=?""",(t[l-1][0],))
                                print("Sucess!")
                                conn.commit()
                                break
                            except ValueError:
                                print("Invalid DataType for serial no.")
                            except IndexError:
                                print("Invalid Index")
                    else:
                        print("No tasks added yet! Please add tasks")
                elif choice_tasks_menu==5:
                    conn.close()
                    return
                else:
                    print("Invalid Choice.")
                    conn.close()
                    return
                break
            except ValueError:
                print("Invalid DataType for choice!")
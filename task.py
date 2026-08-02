import database
import auth
import storage
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
        while True:
            try:
                choice_tasks_menu=int(input("Enter your choice: "))
                if choice_tasks_menu==1:
                    while True:
                        try:
                            if len(database.subject_uni[auth.usercode])!=0:
                                task=input("Enter your task: ")
                                for i in range (len(database.subject_uni[auth.usercode])):
                                    print("Your subjects: \n",i+1,database.subject_uni[auth.usercode][i])
                                k=int(input("Whats the task subject? "))
                                subje=database.subject_uni[auth.usercode][k-1]
                                diction_task={"name":task,"subject":subje,"completed":False}
                                database.tasks_uni[auth.usercode].append(diction_task)
                                print("Task Added Sucessfully!")
                                storage.save_data()
                                break
                            else:
                                print("Add subjects first to write tasks!")
                        except IndexError:
                            print("Invalid choice for serial number!Try again")

                elif choice_tasks_menu==2:
                    print("=============YOUR TASKS================")
                    if len(database.tasks_uni[auth.usercode])!=0:

                        for task in database.tasks_uni[auth.usercode]:
                            if task["completed"]:
                                print("✅", task["name"],"\nSubject: ",task["subject"])
                            else:
                                print("❌", task["name"],"\nSubject: ",task["subject"])
                    else:
                        print("No tasks added yet!")
                elif choice_tasks_menu==3:
                    p=True
                    if len(database.tasks_uni[auth.usercode])==0:
                        p=False
                    if p:
                        for i in range(len(database.tasks_uni[auth.usercode])):
                            if not database.tasks_uni[auth.usercode][i]["completed"]:
                                print("Following are the unfinished tasks: ",i+1,database.tasks_uni[auth.usercode][i]["name"])
                        while True:
                            try:

                                z=int(input("Enter the task you want to mark complete: "))
                                database.tasks_uni[auth.usercode][z-1]["completed"]=True
                                print("✅Task mark completed successfully!")
                                storage.save_data()
                                break
                            except ValueError:
                                print("Invalid DataType")
                            except IndexError:
                                print("Please enter the correct task number!")
                    else:
                        print("No task added yet!")
                elif choice_tasks_menu==4:
                    if len(database.tasks_uni[auth.usercode])!=0:
                        print("These are the current tasks.")
                        for i in range(len(database.tasks_uni[auth.usercode])):
                            print(i+1,database.tasks_uni[auth.usercode][i]["name"])
                        while True:
                            try:
                                l=int(input("Enter the serial no. of the task you want to delete: "))
                                database.tasks_uni[auth.usercode].pop(l-1)
                                storage.save_data()
                                print("Sucess!")
                                break
                            except ValueError:
                                print("Invalid DataType for serial no.")
                            except IndexError:
                                print("Invalid Index")    
                    else:
                        print("No tasks added yet! Please add tasks")
                elif choice_tasks_menu==5:
                    return
                else:
                    print("Invalid Choice.")
                    return
                break
            except ValueError:
                print("Invalid DataType for choice!")

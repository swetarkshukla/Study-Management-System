import auth
import sqlite3
def progress():
    conn=sqlite3.connect("study.db")
    cursor=conn.cursor()
    completed_tasks_counter=0
    incomplete_tasks_counter=0
    print("===========PROGRESS===============")
    cursor.execute("""SELECT * FROM Tasks WHERE User_ID=?""",(auth.user_id,))
    task=cursor.fetchall()
    print("Total Tasks: ",len(task))
    for entries in task:
        if entries[4]==1:
            completed_tasks_counter+=1
        else:
            incomplete_tasks_counter+=1
    print("Completed Tasks: ",completed_tasks_counter)
    print("Incomplete Tasks: ",incomplete_tasks_counter)
    if len(task)!=0:
        completion_rate=(completed_tasks_counter/len(task))*100
        print("Completion Rate: ",completion_rate,'%')
        if completion_rate==100.0:
            print("Yeyyy! You are all done 🥳")
        elif 76.0<completion_rate<=99.0:
            print("Amazing!!! You are about to reach your goal 🔥🔥🔥")
        elif 50.0<completion_rate<=76.0:
            print("Keep grinding!!!!!!! You got this 🔥🔥")
        elif 26.0<completion_rate<=50:
            print("Your progress is compounding!!!!!!! Keep moving 🔥")
        elif 1.0<=completion_rate<=26.0:
            print("Its never too late to start, you got this 😤")
        else:
            print("Completion rate: 0%")
            print('''📚 No tasks yet!
Let's add your first task and start your study journey!''')
    print("---------SUBJECT PROGRESS-----------")
    cursor.execute("""SELECT * FROM Subjects WHERE User_ID=?""",(auth.user_id,))
    sub=cursor.fetchall()
    for ele in sub:
        comp=0
        total=0
        for elee in task:
            if elee[2]==ele[1]:
                total+=1
                if elee[4]==1:
                    comp+=1
        print(ele[1],":",comp,'/',total,'completed')
    conn.close()
import database
import auth
def progress():
    completed_tasks_counter=0
    incomplete_tasks_counter=0
    print("===========PROGRESS===============")
    print("Total Tasks: ",len(database.tasks_uni[auth.usercode]))
    for t in database.tasks_uni[auth.usercode]:
        if t["completed"]:
            completed_tasks_counter+=1
        else:
            incomplete_tasks_counter+=1
    print("Completed Tasks: ",completed_tasks_counter)
    print("Incomplete Tasks: ",incomplete_tasks_counter)
    if len(database.tasks_uni[auth.usercode])!=0:
        completion_rate=(completed_tasks_counter/len(database.tasks_uni[auth.usercode]))*100
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
    for ele in database.subject_uni[auth.usercode]:
        comp=0
        total=0
        for elee in database.tasks_uni[auth.usercode]:
            if elee['subject']==ele:
                total+=1
                if elee['completed']:
                    comp+=1
        print(ele,":",comp,'/',total,'completed')
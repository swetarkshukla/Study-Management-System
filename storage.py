import json
import database
def load_data():
    try:
        with open("data_study_planner.json","r") as file:
            data = json.load(file)
            database.username=data.get("Username",[])
            database.password=data.get("Password",[])
            database.name=data.get("Name",[])
            database.course=data.get("Course",[])
            database.semester=data.get("Semester",[])
            database.cgpa_target=data.get("Targeted CGPA",[])
            database.subject_uni=data.get("Subjects",[])
            database.tasks_uni=data.get("Tasks",[])
    except FileNotFoundError:
        print("No saved data found.")    
    except json.JSONDecodeError:
        print("Invalid saved data! Moving forward with empty data.")
def save_data():
    data={"Username": database.username,"Password":database.password,"Name":database.name,"Course": database.course, "Semester": database.semester, "Targeted CGPA": database.cgpa_target, "Subjects": database.subject_uni, "Tasks": database.tasks_uni}
    with open("data_study_planner.json","w") as file:
        json.dump(data,file,indent=2)
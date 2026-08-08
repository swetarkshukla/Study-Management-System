import sqlite3
conn = sqlite3.connect("study.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT UNIQUE, Password TEXT, Name TEXT, Course TEXT, Semester INTEGER, Target_CGPA REAL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects(User_ID INTEGER , Subject TEXT, FOREIGN KEY (User_ID) REFERENCES Users(ID))""")
cursor.execute("CREATE TABLE IF NOT EXISTS Tasks(Task_ID INTEGER PRIMARY KEY AUTOINCREMENT,User_ID INTEGER, Subject TEXT, Task TEXT, Completed INTEGER, FOREIGN KEY (User_ID) REFERENCES Users(ID))")
conn.commit()
conn.close()
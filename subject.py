import auth
def subjects():
    while True:
        print('''==============================================
                SUBJECTS
==============================================
1.Add Subject
2.View Subjects
3.Remove Subjects
4.Back''')
        import sqlite3
        conn= sqlite3.connect("study.db")
        cursor=conn.cursor()
        while True:
            try:
                choice_subjects_menu=int(input("Choice: "))
                if choice_subjects_menu==1:
                    subj=input("Enter your subject: ")
                    cursor.execute("""SELECT * FROM Subjects WHERE User_Id=?""",(auth.user_id,))
                    check = cursor.fetchall()
                    found = True
                    for ele in check:
                        if subj==ele[1]:
                            print("Subject already exists!")
                            found=False
                        else:
                            break
                    if found:
                        cursor.execute("""INSERT INTO Subjects(User_ID, Subject) VALUES(?,?) """,(auth.user_id, subj))
                        conn.commit()
                    print("Subject added sucessfully!")
                elif choice_subjects_menu==2:
                    cursor.execute("SELECT * FROM Subjects WHERE User_Id=?",(auth.user_id,))
                    check=cursor.fetchall()
                    if not check:
                        print("No subjects added yet.")
                    print("============YOUR SUBJECTS==============")
                    for ele in check:
                        print("Subjects: ", ele[1])
                elif choice_subjects_menu==3:
                    cursor.execute("SELECT * FROM Subjects WHERE User_Id=?",(auth.user_id,))
                    check=cursor.fetchall()
                    k=True
                    print("Your current subjects are: ")
                    for ele in check:
                        print(ele[1])
                    sub_remove=input("Enter the subject you want to remove: ")
                    for ele in check:
                        if sub_remove==ele[1]:
                            cursor.execute("""DELETE FROM Subjects WHERE User_Id =? AND Subject=?""",(auth.user_id, sub_remove))
                            conn.commit()
                            print("Subject removed successfully!")
                            k=False
                            break
                    if k:
                        print("Subject not found!")
                elif choice_subjects_menu==4:
                    return
                else:
                    print("Invalid Choice!")
                break
            except ValueError:
                print("Invalid DataType for choice")
        conn.close()
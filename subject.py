import database
import storage
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
        while True:
            try:
                choice_subjects_menu=int(input("Choice: "))
                if choice_subjects_menu==1:
                    subj=input("Enter your subject: ")
                    database.subject_uni[auth.usercode].append(subj)
                    storage.save_data()
                    print("Subject added sucessfully!")
                elif choice_subjects_menu==2:
                    if len(database.subject_uni[auth.usercode])==0:
                        print("No subjects added yet.")
                    print("============YOUR SUBJECTS==============")
                    for ele in database.subject_uni[auth.usercode]:
                        print("Subjects:",ele)
                elif choice_subjects_menu==3:
                    k=True
                    print("Your current subjects are: ", database.subject_uni[auth.usercode])
                    sub_remove=input("Enter the subject you want to remove: ")
                    for ele in database.subject_uni[auth.usercode]:
                        if sub_remove==ele:
                            database.subject_uni[auth.usercode].remove(ele)
                            print("Subject removed successfully!")
                            k=False
                            break
                    if k:
                        print("Subject not found!")
                    storage.save_data()
                elif choice_subjects_menu==4:
                    return
                else:
                    print("Invalid Choice!")
                break
            except ValueError:
                print("Invalid DataType for choice")
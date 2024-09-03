Att=int(input("ENTER ATTENDENCE"))
if Att>=75:
    print("STUDENT CAN TAKE EXAM")
else:
    Y=input("Was student absent for medic condition")
    if Y=="yes":
        print("STUDENT CAN TAKE EXAM")
    else:
        print("STUDENT CANNOT TAKE EXAM")
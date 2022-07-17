from statistics import mean as m

admins = {"python":"pass123@","user2":"pass2"}

studentDict = {
    "sam":[78,88,98],
    "mike":[98,88,80],
    "mano":[89,90,99]
}


def enterGrades() :
    nameToEnter = input("Student Name: ")
    gradeToEnter = input("Grade: ")
    
    if nameToEnter in studentDict:
        print("Adding Grade...")
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print("student does not exist.")
        print(studentDict)
        
def removeStudent():
    nameToRemove =input("what student to remove?: ")
    if nameToRemove in studentDict:
        print("removing studuent...")
        del studentDict[nameToRemove]
        
        print(studentDict)
def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent,"has an average grade of :" ,avgGrade)
    

def main():
    print("""
          Welcome to Grade Central
          [1] - Enter Grades
          [2] - Remove Student
          [3] - Student Average Grades
          [4] - Exit
          """)
    
    action = input("what would you like to do today? (enter a number) ")
    if action == "1":
      enterGrades()
    elif action =="2":
        removeStudent()
    elif action == "3":
        print("studentAVGs")
    elif action == "4":
        exit()   
    else:
        
        print("No valid choice was given, try again")
login = input("username: ")
passw = input("password: ")

if login in admins:
    if admins(login) == passw:
        print("Welcome",login)
        while True:
         main()
    else: 
        print("invalid password, will denote in 5 seconds")
else:
    print("invalid username,calling the FBI to report this")



class Student:
    def __init__(self, name, age, grade):
     self.name = name
     self.age = age
     self.grade = grade #1-100
     
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        #add a method that gonna allow us to students to the course.
        # we gonna do that by have a student list
        self.students = [] #list of students
        #this method gonna add students to the Course
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_garde()
            return value / len(self.students)
        
        
        s1 = Student("sammy",20,98)
        s2 = Student("zalo",21,75)
        s3 = Student("Priscilla",19,65)
        s4 = Student ("Edwin",22,65)
        course = Course("computer",2)
        course.add_student(s1)
        course.add_student(s2)
        print(course.get_average_grade())
        
    
    
        
        
            
     
     
     
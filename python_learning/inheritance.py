class Pet :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        def show(self):
            print(f"am{self.name} and {self.age} old")

class Cat(Pet):
    #def __init__(self,name,age):
        #self.name = name
       # self.age = age
    def speak(self):
     print("meow")
    
class Dog(Pet):
    #def __init__(self,name,age):
        #self.name = name
        #self.age = age
    def speak(self):
        print("bark")    
               
#p = Pet("sam",19)
#p.show()
c = Cat("tracey",20)
c.speak()
d = Dog ("zalo",22)
d.speak()

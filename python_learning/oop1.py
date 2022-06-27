#class
from inspect import Attribute


class SoftwareEngineer:
    
    def __init__(self,name,age,level,salary):
        #instances Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        #s1 = ["Software Engineer","sam",20,"junior",7000]
        
    se1 = SoftwareEngineer ("sam",22,"senior",7000)
    print(se1.name,se1.age)
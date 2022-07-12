class Dog :
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type
       # print(name)
    
    #def add_one(self,x):
    def get_name(self):
      return self.name
    def get_age(self):
      return self.age
    def get_type(self):
        return self.type
    def set_age(self,age)
     self.age = age
  
    '''def bark(self):
        print("bark")'''
        
d = Dog("sammy",12,"chawawa")
print(d.get_type())

d2 = Dog("manoah",14,"shephard")
print(d2.get_type())

d3 = Dog("sanchez",16,"normal")
print(d3.get_type())

    
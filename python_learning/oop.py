class Person:
    def __init__(self,first_name):
       # self.last_name = last_name
        self.first_name = first_name
    def say_hi(self):
        print('hi',self.first_name)
   #     print('welcome',self.last_name)
   #pass  empty block
p = Person("Manoah")
say_hi()



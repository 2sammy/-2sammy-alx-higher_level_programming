from multiprocessing.connection import answer_challenge
from tkinter import Y


class Calc:
    def add(x,y):
      answer = x+y
      print(answer)
      
    def Sub(x,y):
        answer = x-y
        print(answer)
      
    def multi(x,y):
        answer = x*y
        print(answer)
        
    def div(x,y):
        answer = x/y 
        print(answer)
        
Calc.add(8,2)
Calc.div(8,2)
Calc.multi(8,2)
Calc.Sub(8,2)
                 
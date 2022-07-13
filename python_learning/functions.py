#def #notifies the python its a function
'''def example():
    x = 3
    y = 4
    print(x+y)
    
    if x < y:
        print(x,"is less than",y)
    
    example()'''
    #functions parameters
from tkinter import Variable


def addition(num1,num2,num3,num4):
        answer = num1 + num2 + num3
        return answer
x = addition(5,5,5,5)
print(x)

def subract(di1,d2,d3,d4):
    result = di1-d2-d3-d4
    return result
y = subract(30,10,5,0)
print(y)

def website(font,background_color,font_color,font_size):
    print("font:",font)
    print("bg:",background_color)
    print("font size:",font_size)
    print("font color:",font_color)

website("serif thin","blue","black","12")

def application (font_family,background_color,font_size,login_picture):
    print("font family:",font_family)
    print("backcolor:",background_color)
    print("font size:",font_size)
    print("picture:",login_picture)
    
application("serif","yellow","14","football")
#global Variable vs local variable
x = 6 #global
def example():
    z= 5 #local




    
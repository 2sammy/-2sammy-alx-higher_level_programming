'''name = input("what is your name?: ")
print("hello",name)
'''
import statistics
exList = [9,8,7,6,5,4,3,2,1]
x= statistics.mean(exList)
print(x)
x = statistics.median(exList)
print(x)
x= statistics.mode(exList)
print(x)
x = statistics.stdev(exList)
print(x)
x = statistics.variance(exList)
from functools import reduce

list=[1,2,3,4,5,6,9]
num=reduce(lambda a,b: a+b,list)
print(num)
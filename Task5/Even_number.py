num=[1,2,3,4,5,6,7,8,9,10]
even_number=list(map(lambda x:x*x,filter(lambda x: x%2==0,num)))
print("Even numbers in the list is:",even_number)
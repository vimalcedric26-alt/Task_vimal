list=[1,2,3,4,1,2,5,6]
non_numb=[]
for i in list:
    if i not in non_numb:
        non_numb.append(i)

print("Non-repeating numbers:", non_numb)
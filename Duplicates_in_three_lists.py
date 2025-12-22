list1=[1,2,3,4,5]
list2=[2,3,4,6,7]
list3=[0,1,2,3,4,6]
duplicate=[]
for i in list1:  #check in list1
    if i in list2 and i in list3:  #check in list2 and list3
        duplicate.append(i)      #Adds same number to duplicate list

print("List of duplicates is:",duplicate)


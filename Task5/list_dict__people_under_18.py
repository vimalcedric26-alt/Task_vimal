my_dict={'prem':12, 'santosh':15,"satish":17,'dani':20,'peter':30}
age=dict(filter(lambda items: items[1]<=18,my_dict.items()))
print(age)
new_list=list(map(lambda items: items[0],age.items()))
print(new_list)

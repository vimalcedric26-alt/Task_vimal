lst = [4,1,2,3,5,0,8,6,7]

minimum = lambda x: min(x)
print("Minimum value is:",minimum(lst))
sorted_list = sorted(lst, key=lambda x: x)
print("Sorted list:",sorted_list)
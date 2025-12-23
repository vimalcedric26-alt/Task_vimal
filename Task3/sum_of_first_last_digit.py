from functools import reduce
add_ = lambda a, b: a + b     # Lambda function that adds two numbers
lst = [1, 2, 3, 4, 5]
print(reduce(add_, lst, 10))  # reduce adds all numbers in lst starting from 10
num=[10,501,2237,100,999,87,351]
prime_numbers=[]
for n in num: #To check number from the list and store variable in n
    if n>1:#n is greater than 1
        for i in range(2,int(n**0.5)+1):#converting to integer because range() needs integers and +1 is for the last number.
         if n%i==0:
                    break
        else:
            prime_numbers.append(n)
            print("prime number is :",prime_numbers)

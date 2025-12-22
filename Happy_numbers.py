def is_happy(n):
    seen = set()  # to detect loops

    while n != 1 and n not in seen: #checking if n becomes n=1 or loop will continue
        seen.add(n)                 #adding the current number
        n = sum(int(digit)**2 for digit in str(n)) #square each number,calculate the sum

    return n == 1 #if n=1 return true


num = [10, 501, 2237, 100, 999, 87, 351]
happy_numbers = [n for n in num if is_happy(n)]

print("Happy numbers:", happy_numbers)
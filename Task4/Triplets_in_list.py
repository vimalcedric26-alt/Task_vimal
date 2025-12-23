list = [10, 20, 30, 9]
total = 59

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        for k in range(j + 1, len(list)):
            if list[i] + list[j] + list[k] == total:
                print("Sum equal to the given value 59 is:",list[i], list[j], list[k])
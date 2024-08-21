n = int(input("Enter the size of the box: "))

i = 1

for _ in '*' * n: 
    j = '*' * i
    print(j)
    i += 1
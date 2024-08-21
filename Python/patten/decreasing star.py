n = int(input("Enter the size of the box: "))

i = n

for _ in '*' * n: 
    j = '*' * i
    print(j)
    i -= 1



rows = int(input ("enter the number of rows: "))
i = 1
for i in range(rows):
    print(" "*(rows-i -1)+" *"*(i+1))
for j in range(rows -1):
    print(" "*(j+1)+" *"*(i-j))



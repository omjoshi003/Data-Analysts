size = int(input ("enter the number: "))
i = 0
# i is row set range (0 ,1 ,2 ,3, 4)
# j is col  
# put i annd j if any of conadition true then print * else ""
while i < size:
        j = 0
        while j < size:
            if j == i or j == size - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
            j += 1
        print() 
        i += 1



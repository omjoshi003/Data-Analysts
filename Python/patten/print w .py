
n = int(input("Enter the size: "))

for row in range(1, n+1):
        
        for col in range(n - row + 1):
            print("*", end="")

        for space in range(2 * (row - 1)):
            print(" ", end="")

        for col in range(n - row + 1):
            print("*", end="")

        print()



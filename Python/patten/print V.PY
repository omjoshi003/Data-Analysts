#  end='' argument ensures that the print function does not add a newline after the spaces.
n= int(input("Enter the number: "))
    
i = 0
while i < n:
        
        print(' ' * i, end='')
        print('*', end='')
        # one side of * line print after i sapce added 
        if i < n - 1:
            # print space between the 2 * start from n-1
            print(' ' * (2 * (n - i - 1) - 1), end='')
            # Print the right side of V
            print('*')
        else:
            print()
        i += 1


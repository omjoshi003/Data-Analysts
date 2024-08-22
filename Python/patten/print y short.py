#  end='' argument ensures that the print function does not add a newline after the spaces.
n= int(input("Enter the number: "))
    
i = 0
while i < n:
        
        print(' ' * i, end='')
        print('*', end='')
        if i < n - 1:
            # print space between the 2 * start from n-1
            print(' ' * (2 * (n - i - 1) - 1), end='')
            
            print('*')
        else:
            print()
        i += 1
# convert v into y adding 2 line in v shape
if i == n:  
        for _ in range(2):
            print(' ' * (n - 1) + '*')
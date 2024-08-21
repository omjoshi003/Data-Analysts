n = int(input("Enter the number: "))

stars = 1
spaces = n - 1

for _ in '*' * n:  
    
    print(' ' * spaces + '*' * stars)
    spaces -= 1
    stars += 2

n = int(input("Enter the number odd number:  "))

i = 0
while i < n:
    if i < n // 2:
        # Print the upper part of Y like v
        print(' ' * i + '*' + ' ' * (n - 2 * i - 2) + '*')
    elif i == n // 2:
        # for center part where v and straigth line divide
        print(' ' * i + '*')
    else:
        # for center line n diveded by 2 and print *
        print(' ' * (n // 2) + '*')
    i += 1

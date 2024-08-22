n = int(input('Enter the number: '))

def pyramid(n):
    for i in range(n):
        if i == 0:
            print(' ' * (n - i - 1) + '*')
        else:
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

pyramid(n)

def inverted_pyramid(n):
    for j in range(n):
        if j < n - 1:
            print(' ' * j + '*' + ' ' * (2 * (n - j - 1) - 1) + '*')
        else:
            print(' ' * j + '*')

inverted_pyramid(n)
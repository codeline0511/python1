def display_triangle(height):
    for i in range(1, height + 1):
        display_num(i)
        print()

def display_num(n):
    for i in range(1, n+1):
        print(i, end = '')

h =int(input('높이?'))
display_triangle(h)

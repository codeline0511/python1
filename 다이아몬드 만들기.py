def draw_diamond(ch, height):
    for i in range(1, height + 1):
        draw_line1(ch, i)
        draw_line2(ch, i)
        print()

    for i in range(1, height + 1):
        draw_line3(ch, i)
        draw_line4(ch, i)
        print()

def draw_line1(ch, n):
    print(ch * (h - n + 1), end = '')
    print(' ' * (n-1), end = '')

def draw_line2(ch, n):
    print(' ' * (n-1), end = '')
    print(ch * (h - n + 1), end = '')

def draw_line3(ch, n):
    print(ch * n, end ='')
    print(' ' * (h - n), end = '')

def draw_line4(ch, n):
    print(' ' * (h - n), end = '')
    print(ch * n, end ='')

char = input('모양?')
h = int(input('높이?'))
draw_diamond(char, h)

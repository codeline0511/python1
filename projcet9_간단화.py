def draw_triangle(height, ch ='*'):
    for i in range(1, height+1):
        draw_line(ch, i)
        draw_line(' ', height - i)
        print()

def draw_line(ch, i):
    print(ch * i, end= '')


h = int(input('높이?'))
draw_triangle(h)

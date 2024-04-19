def display_triangle(height, ch = '*'):
    for i in range(1, height + 1):
        draw_line(' ', height - i)
        draw_line(ch, i)
        print()        


def draw_line(ch, n):
    #for i in range(1, h+1):
        #print('*',end = '')
    print(ch * n, end = '')

h =int(input('높이?'))
display_triangle(h)

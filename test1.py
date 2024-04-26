def display_quad(height):
    ch = '*'
    for i in range(1, height + 1):
        if (i==1 or i == height):
            print(ch * height, end ='')
            print()
            
        else:
            print(ch, end = '')
            print(' '*(height -2), end= '')
            print(ch, end='')
            print()

height= int(input('높이? '))
display_quad(height)

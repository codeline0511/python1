def again_set(n):
    for i in range(3):
        for j in range(1, n+1):
            print(j, end= ' ')
        print()
            
num = int(input('몇번 하실 건가요?'))
again_set(num)

print()
def number_set(n, m):
    for i in range(1, m+1):
        print(f'{n} x {i} = {n * i:2d}')

    #i = 1
    #while i <= m:
    #   print(f'{n} x {i} = {n * i:2d}')
    #   i += 1
    #while문을 이용한 경우, for문과 비슷하나 i의 시작값을 정해주어야 함

number = int(input('출력할 곱셈단을 양의 정수로 입력하세요:'))
again = int(input('곱셈단의 범위를 정해주세요:'))
number_set(number, again)

print()
def high_number(n):
    for i in range(1, n+1): # 반복되는 횟수
        display_num(i)
        print()
            
def display_num(n):
    for i in range(1, n+1): #출력되는 수의 갯수 
        print(i, end ='')

num = int(input('높이?'))
high_number(num)


print()
def display_triangle(height, ch = '*'):
    for i in range(1, height + 1): # 1~height번째까지 출력
        draw_line(' ', height - i) # 공백을 height-1개 출력
        draw_line_under(ch, i) # 원하는 모양을 i개 출력
        print()

def draw_line(ch, n):
    print('|' * h,end = '')
    print(ch * n, end = '')

def draw_line_under(ch, n):
    print(ch * n, end ='')
    print('|' * h,end = '')

h =int(input('높이?'))
display_triangle(h)

def input_positive_number(promt):
    n = 0
    while n <= 0:
        n = int(input(promt))


    return n

def display_multiplication_table(n): #while문 이용 
    i = 1
    while i <= 9:
        print(f'{n} * {i} = {n * i}')
        i += 1

number = input_positive_number('출력할 구구단을 양의 정수로 입력하세요:')

display_multiplication_table(number)

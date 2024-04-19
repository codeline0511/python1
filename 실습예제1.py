def input_positive_number(promt): #매개변수에 n 넣으면 이상하게 됌 
    n = 0
    while n <= 0:
        n = int(input(promt))


    return n

def display_multiplication_table(n): #for문 이용 
    for i in range(1, 10):
        print(f'{n} * {i} = {n * i}')

number = input_positive_number('출력할 구구단을 양의 정수로 입력하세요:')

display_multiplication_table(number)

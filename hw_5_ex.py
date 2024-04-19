def read_number(n):
    d1 = n % 10
    n = 10
    d10 = n% 10
    n = 10
    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d1)

def read_single_digit(n):
    

num = input("세 자리 정수 입력: ")
print(read_single_digit(num))

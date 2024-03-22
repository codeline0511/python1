n3 = int(input("피젯수를 정수로 입력하세요:"))
n4 = int(input("젯수를 정수로 입력하세요:"))


def show_divison(dividend, divisor):
    quotient = dividend// divisor
    
    remainder = dividend % divisor
    
    print('몫 =', quotient)
    print('나머지 =', remainder)


show_divison(dividend = n3, divisor = n4)



#show_divison(n1, n2)
#n1 = int(input("피젯수를 정수로 입력하세요:"))
#n2 = int(input("젯수를 정수로 입력하세요:"))
#(show_division(n1, n2))


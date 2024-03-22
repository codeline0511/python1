dividend_1 = int(input("피젯수를 정수로 입력하세요:"))
divisor_1 = int(input("젯수를 정수로 입력하세요:"))
a = dividend_1 // divisor_1
b = dividend_1 % divisor_1
print("몫 =", a, "\n나머지 =", b, "\n")

n1 = 0b10101101 
n2 = 0b00001111

print(bin(n1 & n2))
print(bin(n1 | n2))
print(bin(n1 ^ n2))
print(bin(~n2))
print(bin(n2 >> 2))
print(bin(n2 << 2), "\n")
    
n3 = int(input("피젯수를 정수로 입력하세요:"))
n4 = int(input("젯수를 정수로 입력하세요:"))


def show_divison(dividend, divisor):
    quotient = dividend// divisor
    
    remainder = dividend % divisor
    
    print('몫 =', quotient)
    print('나머지 =', remainder)


show_divison(dividend = n3, divisor = n4)

total_cost = int(input('\n구매한 물건의 총구매 금액은?'))
payment = int(input('고객으로부터 지불받은 금액은?'))
change = payment - total_cost

def show_change(amount):
    print('잔돈:', amount, '원')
    
    n5000 = amount // 5000
    amount %= 5000

    n1000= amount // 1000
    amount %= 1000

    print('> 5000원권', n5000, '장')
    print('> 1000원권', n1000, '장')
    print('남은 금액:', amount, '원')

show_change(change)

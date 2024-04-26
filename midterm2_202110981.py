def shift0p(a, n, isLeftDirection):
    if isLeftDirection == True:
        a_1 = a * (2**n)
        print(f'{a}<<{n} = {a_1} ({bin(a_1)})')

    if isLeftDirection == False:
        a_2 = a // (2**n)
        print(f'{a}>>{n} = {a_2} ({bin(a_2)})')
        

print('비트단위 시프트 연산(a<<n 및 a>>n) 프로그램')
a1 = int(input('a를 입력하세요: '))
n1 = int(input('n을 입력하세요: '))
shift0p(a1, n1, isLeftDirection = True)
shift0p(a1, n1, isLeftDirection = False)


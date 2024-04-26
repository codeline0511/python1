# 주사위를 원하는 만큼 돌려 모든 경우에 나오는 수를 출력 ->반복문 for 사용
# 주사위의 수 1~6까지 나온 횟수를 전부 더하고 출력 ->반복문 while, 조건문 if 사용
# 확률까지 계산 -> 자릿수 제한 {:'n'g} 사용
import random

def roll_dice(n):
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    
    for i in range(1, m+1):
        if (i % 3) == 0 and i != m :
            n = random.randint(1, 6)
            print(f'{i}번째 주사위의 수:{n}', end = '\t')
            print()
            print()

        elif i == m:
            n = random.randint(1, 6)
            print(f'{i}번째 주사위의 수:{n}', end = '\t')
            print()
            
        else :
            n = random.randint(1, 6)
            print(f'{i}번째 주사위의 수:{n}', end = '\t')

        if n == 1:
            n1 += 1
        elif n == 2:
            n2 += 1
        elif n == 3:
            n3 += 1
        elif n == 4:
            n4 += 1
        elif n == 5:
            n5 += 1
        else :
            n6 += 1       

    print(f'\n1이 나온 횟수:{n1:2d}번, 확률 계산: {n1:2d} / {m} = {n1 / m:.2g}')
    print(f'2가 나온 횟수:{n2:2d}번, 확률 계산: {n2:2d} / {m} = {n2 / m:.2g}')
    print(f'3이 나온 횟수:{n3:2d}번, 확률 계산: {n3:2d} / {m} = {n3 / m:.2g}')
    print(f'4가 나온 횟수:{n4:2d}번, 확률 계산: {n4:2d} / {m} = {n4 / m:.2g}')
    print(f'5가 나온 횟수:{n5:2d}번, 확률 계산: {n5:2d} / {m} = {n5 / m:.2g}')
    print(f'6이 나온 횟수:{n6:2d}번, 확률 계산: {n6:2d} / {m} = {n6 / m:.2g}')

m = int(input('몇번 돌리시겠습니까?'))
roll_dice(m)

    




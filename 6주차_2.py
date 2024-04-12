# 코드1
n1 = int(input('첫 번째 정수는?'))
n2 = int(input('두 번째 정수는?'))

if n1 > n2 : print(f'{n1}은(는) {n2} 보다 크다')

if n1 > n2 :
    print(f'{n1}은(는) {n2} 보다 크다')

if n1 > n2 :
    print(f'{n1}은(는) {n2} 보다', end = ' ')
    print('크다')

if n1 <= n2 :
    print(f'{n1}은(는) {n2} 보다 크지 않다') # 상호 배타적인 조건문 

print('끝\n')

# 코드2
n3 = int(input('첫 번째 정수는?'))
n4 = int(input('두 번째 정수는?'))

if n3 > n4 :
    print(f'{n3}은(는) {n4} 보다 크다')
else :
    print(f'{n1}은(는) {n2} 보다 크지 않다')

print('끝\n')

# 코드3(실습예제)
num = int(input('정수를 입력하세요:'))

if num % 2 == 0 :
    print(f'{num}은(는) 짝수입니다.')
else :
    print(f'{num}은(는) 홀수입니다.')

# 코드3_1
num = int(input('\n정수를 입력하세요:'))

print(f'{num}은(는)', end = ' ')
if num % 2 == 0 :
    print('짝수', end = '')
else :
    print('홀수', end = '')
print('입니다.')

# 코드3_2 -> 실습예제1로 이동 


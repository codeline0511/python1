# 코드 1
n1 = int(input('첫 번째 정수는? '))
n2 = int(input('두 번째 정수는? '))
print(f'(n1)와 (n2)의 평균은 {(n1 + n2) / 2}\n')

# 코드 2
num = int(input('정수는? '))

print(f'2진 표현으로는 {num:b}입니다.')
print(f'10진 표현으로는 {num:d}입니다.')
print(f'16진 표현으로는 {num:x}입니다.\n')

# 코드 3
n3 = int(input('첫 번째 정수는? '))
n4 = int(input('두 번째 정수는? '))

avg = n3 / n4

print(f'{n3} / {n4} = {avg}')
print(f'{n3} / {n4} = {avg:f}')
print(f'{n3} / {n4} = {avg:e}')
print(f'{n3} / {n4} = {avg:g}\n')

# 코드 4
num1 = 15

print(f'[{num1:d}]')
print(f'[{num1:5d}]') # 5자리 확보
print(f'[{num1:<5d}]')
print(f'[{num1:^5d}]')
print(f'[{12345678:5d}]') # 모자라면 지정된 자릿수 무시
print(f'[{num1:05d}]\n')

PI = 3.14159265

print(f'[{PI:f}]') # 기본적으로 소수점 이하 여섯 자리
print(f'[{PI:.2f}]') # 소수점 이하 두 자리
print(f'[{PI:5.2f}]') # 소수점 기호 .도 한 자리를 차지
print(f'[{PI:.2g}]\n') # 유효자리가 두 자리 

# 코드 5
print("'Today is %d %s.'" % (3, 'April'))
print("'Hello, {0} {2} {1}'".format('Python', 'Script', 3.6))
print("'{0} {0} {1} {1}'".format('Python', 'Script'))
print("'Hello, {language} {version}'".format(language = 'Python', version = 3.6))






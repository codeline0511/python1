# 코드1(실습예제2의 다른 버전)
num = int(input('정수를 입력하세요:'))

if num == 0 :
    print(f'{num}', end = '')
elif num < 0 : 
    print('음수', end = '')
else :
    print('양수', end = '')
print('입니다.')

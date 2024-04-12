num = int(input('정수를 입력하세요:'))

if num == 0 :
    print(f'{num}', end = '')
else :
    if num < 0 : # 제어문은 또다른 제어문을 포함할 수 있음/중첩 if문 
        print('음수', end = '')
    else :
        print('양수', end = '')
print('입니다.')

    

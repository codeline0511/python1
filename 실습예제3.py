def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        return True
    else :
        return False


while True:
    y = int(input('윤년 여부를 확인한 연도는?'))

    if is_leap_year(y):
        print(f'{y}년은 윤년입니다.')
    else:
        print(f'{y}년은 평년입니다.')

    rep = input('다른 연도도 확인하겠습니까?')
    if rep != 'Y' and rep != 'y':
        break
    
    print()

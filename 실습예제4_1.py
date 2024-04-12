def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        return True
    else :
        return False


year = int(input('윤년 여부를 확인할 연도는?'))
print(f'{year}년은', end = ' ')
if is_leap_year(year) :
    print('윤년입니다.')
else :
    print('평년입니다.')

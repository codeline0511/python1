def is_leap_year(a):
    if a % 4 == 0 and a % 100 != 0:
        return '윤년'
    elif a % 400 == 0:
        return '윤년'
    else:
        return '평년'

year = int(input('윤년 여부를 확인할 연도는?'))

leap_year = is_leap_year(year)

print(f'{year}년은 {leap_year}입니다.')

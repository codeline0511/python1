from 실습예제4_1 import is_leap_year as LY

def month_days(a, b):
    if (LY(a) == True) and (b == 2):
        return '29'
    elif (LY(a) == False) and (b == 2):
        return ' 28'
    elif (b <= 7 and b % 2 ==1) or (b >= 8 and b % 2 == 0):
        return '31'
    else:
        return '30'

year_1 = int(input('연도?'))
month = int(input('월?'))
print(f'{year}년 {month}월은 {month_days(year_1, month)}일까지 있습니다.')

#계속 실습예제4_1의 year 입력문이 나옴, 수정 요망 

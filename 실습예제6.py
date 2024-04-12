def input_age(age):
    n = int(input(age))
    if n >= 0 and n <= 120:
        return n
    else:
        return -1

def is_adult(a):
    if a >= 19:
        return True
    else:
        return False

age_1 = input_age('나이?')

if age_1 >= 0:
    if is_adult(age_1):
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')

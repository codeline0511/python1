from Boolean import boolean_front_number as front
from Boolean import boolean_back_number as back
from Boolean import boolean_only_one as oo

for i in range(1, 40):
    if i == 20:
        print('모듈 사용 시작', end = '')
    else :
        print('=', end = '')


a = int(input('\n숫자 입력:'))
a_bit = int(input('이동시킬 비트 입력:'))
result = front(a, a_bit)
print('값:', result)

b = int(input('\n숫자 입력:'))
b_bit = int(input('이동시킬 비트 입력:'))
result_1 = back(b, b_bit)
print('값:', result_1)

c = int(input('\n숫자 입력:'))
result_2 = oo(c)
print('값:', result_2)

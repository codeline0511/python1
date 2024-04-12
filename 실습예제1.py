#실습예제 3_2(두 번째 구현)
def is_even_number(a): #정의 함수에서도 조건문 사용 가능 
     if a % 2 == 0 :
         return True
     else :
         return False


num = int(input('\n정수를 입력하세요:'))

print(f'{num}은(는)', end = ' ')
if is_even_number(num) :
    print('짝수', end = '')
else :
    print('홀수', end = '')
print('입니다.')

#if is_odd_number(num) == False:
#if not is_odd_number(num) :
#if is_odd_number(num) :

print(-1+1)

print(0b1010 + 1) # 0b1010 = 2^3=8, 2^1=2

print(0xF + 1) # 0123456789A(10)B(11)C(12)D(13)E(14)F(15)

print(15. + .12345)

print(3.14e-5 + 1)

print(2+3j + 10)

print(not False, False)

print('Hello' + '!')

print()

print('2 + 3 =', 2 + 3)  # ('A') ≠ (A), 문자형과 정수형 

print(2, '+', 3, '=', 2 + 3)

apple, Apple = 1, 2 # 2apple = 2 불가능, 식별자 작성 규칙 위반

print(apple + Apple, 2 * apple)

def show_message() :
    print('Hello world!')
    print('Good job!')

print()
print('시작')
show_message() # 정의된 함수 show_message를 호출 
print('마침')

print()
num = 1004
print(num)

num = '천사'
print(num)
print(type(num))

id(1) # 일반 파일에서는 실행 안됌, IDLE에서 실행요망 

def show_message1(msg, name): #2개 이상의 매개변수를 갖는 함수 
    print(msg, name, '님')
    
print()
print('시작')
show_message1('안녕', '이찬수'),# =-> show_message1(msg='안녕', name='이찬수')
show_message1('반가워', '홍길동'), # =↓show_message1(name='이찬수', msg='안녕')
print('마침')


def show_message2(msg='안녕하세요', name='여러분'):
    print(msg, name, '님')

print() # 매개변수의 기본값을 갖는 함수
print('시작')
show_message2('안녕', '이찬수')
show_message2('안녕')
show_message2()
show_message2(name='이찬수')
show_message2(msg='안녕')
print('마침')

print() #print()의 키워드 인수
print('안녕', '여러분', sep='', end='\n')
print('안녕', '여러분')

print('안녕', '여러분', sep=',')
print('안녕', '여러분', end='!')
print('끝')

def show_message3():
    print('Hello')
    return 'good bye'

print('\n시작')
show_message3() # <-반환값의 부적절한 사용
result = show_message3() # 반환값의 전달 
print(result)
print('마침')

print('\n당신의 이름은?', end ='') # 입력문
name = input()
print('반가워요', name)

name = input('당신의 이름은?\n') # 위의 입력문과 동일, 코드간략 
print('반가워요', name)

def make_message(): # 유형1:매개변수와 반환값을 갖지 않는 함수 
    name = input('당신의 이름은?')
    msg= print('반가워요', name)

print('\n시작')
make_message()
print('마침')

def make_message1(name): # 유형2:매개변수만 갖는 함수
    msg = print('반가워요', name)

print('\n시작')
input_name = input('당신의 이름은?')
make_message1(input_name)
print('마침')

def make_message2(): # 유형3:반환값만 갖는 함수 
    name = input('\n당신의 이름은?')
    msg = '반가워요' + name
    return msg 

result = make_message2()
print('만나게 되어', result)
print(result, '좋은 인연 만들어가요')

def make_message3(name): # 유형4:매개변수와 반환값을 모두 갖는 함수
    msg = '반가워요' + name
    return msg

print('\n시작')
input_name = input('당신의 이름은?')
result = make_message3(input_name)
print(result)
print('마침')

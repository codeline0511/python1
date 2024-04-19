def input_age(promt):
    while True:
        n = int(input())
        if age <= 0 or age >=120: 
            return n

def is_adult(age):
    if age >=20 :
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')

    
num = int(input('나이?'))
input_age(num)
#미완성 



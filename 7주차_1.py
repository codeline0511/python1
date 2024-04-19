# 코드1
pwd = input('비밀번호?')

while pwd != '1234':
    pwd = input('비밀번호?')

print('어서오세요, 문이 열렸습니다!')

# 코드2
pwd = '' # 위 코드와 동일, 가독성은 높아짐, 대신 초기화 필요 

while pwd != '1234':
    pwd = input('비밀번호?')

print('어서오세요, 문이 열렸습니다!')

# 코드3
cnt = 0 # cnt = 1
# print(cnt)보다 간단함 

while cnt < 5:
    cnt += 1
    print(cnt)

pwd = ''

while pwd != '01041394723':
    pwd = input('비밀번호?')

print('문 열림')

print()
while True:
    pwd = input('비밀번호?')
    
    if pwd == '01041394723':
        print('문 열림')
        break

cnt = 0
print()

while cnt < 5: # while문은 조건 만족. 보기에만 있는 값만 입력받을 때 사용
    cnt += 1
    print(cnt)

print()
for i in range(0, 10, 1): # for문은 일정 출력문을 반복해서 출력할 때 사용
    print (i+1) # range(start, stop, step)
    

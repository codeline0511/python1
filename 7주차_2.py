# 코드1
msg = 'hello'
for ch in msg:
    print(f'{ch}/', end='')

print()

# 코드2
for i in range(0, 10, 3): # stop 값은 포함하지 않음, start의 값은 포함 
    print(i, end=' ')

print()

for i in range(1 , 5): # step 부분 생략 시 1씩 증가
    print(i, end=' ')

print()

for i in range(20): # start 생략시 0부터 시작 
    print(i, end=' ')

print()

# 코드3
for i in range(1, 10, 2): 
    print(i, end=' ')

print()

for i in range(10, 0, -1):
    print(i, end=' ')

print()

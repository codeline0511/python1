# 코드1
num = 2
name = '홍길동'

with open('data/example.txt', 'w') as file:  # 텍스트 파일에 쓰기
    file.write('1 이찬수\n')                 # 하나의 문자열을 저장 
    file.write(f'{num} {name}\n')

print('end')

# 코드2
with open('data/example.txt', 'r') as file:
    all = file.read()                        # 전체 내용을 하나의 문자열로 반환

print()
print(all)

# 코드3
lines = []
with open('data/example.txt', 'r') as file:
    lines = file.readlines()                 # 각 행 요소에 개행문자가 포함됨 

print()
print(lines)

# 코드4
lines = []
with open('data/example.txt', 'r') as file:
    while True:
        line = file.readline()

        if line == '':
            break

        lines.append(line.strip())  # <-문자열 line 앞뒤의 공백문자 제거 후 리스트 lines에 추가

print()
print(lines)

# 코드5
lines = []
with open('data/example.txt', 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

print()
print(lines)

week = '월화수목금금금요일'
n = week.count('금')
print(n)
m = week.count('월')
print(m)
k = week.count('토')
print(k)

pos = week.find('금') # 왼쪽부터 찾음
pos1 = week.find('월', 3) # 여기서 숫자는 자리를 나타냄, 0부터 시작
pos2 = week.rfind('금') # 오른쪽부터 찾음
print(pos)
print(pos1) # 값이 false(없음)이기 때문에 -1 출력
print(pos2)

def rep_char(ch, n):
    print(f'{ch*n}')

a = input('출력시킬 문자:')
b = int(input('출력시킬 횟수:'))
rep_char(a,b)

def draw_line_string(string):
    char = '-'
    length = int(len(string) * 2 + 4)
    rep_char(char, length)
    print(f'  {string}  ')
    rep_char(char, length)
    
draw_line_string('안녕하세요')

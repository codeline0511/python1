# 코드1
text = 'python'
print('t' in text) # in: 기준문자열이 부분문자열을 포함하나?
print('T' in text)
print('th' in text)
print('티' not in text) # not in: 기준문자열이 부분문자열을 포함하지 않나?
print('o' not in text, '\n')

# 코드2
num = input('정수를 입력하세요:')
length = len(num)
print(f'입력하신 {num}은(는) {length}자리 정수입니다\n')

# 코드3
week = '월화수목금금금'
n = week.count('금')
print(n)

week1 = '월화수목금금금요일' #012345678

pos = week1.find('금')
print(pos)

pos = week1.find('금', 5)
print(pos)

pos = week1.rfind('금')
print(pos)

pos = week1.find('토')
print(pos,'\n')

# 코드4
msg = 'Python은 배우기 쉽다. Python은 강력하다'
res = msg.replace('Python', '파이썬')
print(msg)
print(res)









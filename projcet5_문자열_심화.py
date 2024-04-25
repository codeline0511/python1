def name_cut(name):
    c1 = name[0]
    c2 = name[1:]

    a = '성:\t'+c1
    b = '이름:\t'+c2

    print('-' * (len(b) * 2)) # -를 일정횟수만큼 반복시켜도 되긴 하는데..
    print(f'{a}')
    print(f'{b}')
    print('-' * (len(b) * 2))

your_name = input('당신의 이름은?')
name_cut(your_name)
print()
print('조' in your_name)
print('정' not in your_name)
print('a' in your_name) # 참고로 ''는 항상 True, ' '는 빈칸 인덱스 
print('한흠' in your_name)

# 'Today is %d %s' %(3, 'April') # C언어와 유사하게 서식(format)을 지정 가능
# 'Hello, {0} {2} {1}'.format('Python, 'Script', 3.6) # format 메서드로 값을 넣음
# '{0} {0} {1} {1}.format('Python', 'is fun') # 인덱스는 0부터 시작, 미지정 시 순서대로 넣음

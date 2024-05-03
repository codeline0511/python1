scores = []
print('[점수 입력]')
n1 = int(input('#1? '))
scores.append(n1)

n2 = int(input('#2? '))
scores.append(n2)

n3 = int(input('#3? '))
scores.append(n3)

print(f'\n입력 점수: {n1} {n2} {n3}')
print(f'평균: {(n1 + n2 + n3) / 3:.1f}')


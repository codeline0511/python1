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

print('\n[검색]')
score = int(input('찾고자 하는 점수는? '))
if score in scores:
    print(f'{score}점은 {scores.index(score)+1}번 학생의 점수입니다.')
else:
    print('그런 점수는 존재하지 않습니다.')

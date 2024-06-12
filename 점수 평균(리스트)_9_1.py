scores = []
print('[점수 입력]')
for i in range(3):
    n = int(input(f'#{i + 1}? '))
    scores.append(n)
    
print('\n[점수 출력]')
print(f'입력 점수: {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] + scores[2]) / len(scores)
print(f'평균: {avg:.1f}')

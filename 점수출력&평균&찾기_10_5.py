def input_scores():
    a = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        a.append(n)
        i += 1
    return a

def get_average(a):
    total = 0
    for n in a:
        total += n
    return total / len(a)

def show_scores(a):
    for n in a:
        print(n, end= ' ')
    print()

def search(lst, n):
    if n not in lst:
        return None
    return lst.index(n)

print('[점수 입력]')
scores = input_scores()

print('\n[점수 출력]\n개인점수: ', end='')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')

print('\n[검색]')
s = int(input('찾고자 하는 점수는? '))
idx = search(scores, s)
if idx != None:
    print(f'{s}점은 {idx + 1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')

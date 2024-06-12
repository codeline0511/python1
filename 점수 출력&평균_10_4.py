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

print('[점수 입력]')
scores = input_scores()
print('\n[점수 출력]\n개인점수: ', end='')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')

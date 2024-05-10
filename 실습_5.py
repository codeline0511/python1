def input_scores():
    num = []
    for i in range(1, 1000):
        n = int(input(f'#{i}? '))
        if n >= 0:
            num.append(n)
        else:
            break
        
    return num

def search(lst, n):
    score = int(input('찾고자 하는 점수는?'))
    if score in lst:
        print(f'{score}점은 {lst.index(score)}번 학생의 점수입니다.')
    else:
        print(f'{score}점을 받은 학생은 없습니다.')

score_list = input_scores()

search(score_list)

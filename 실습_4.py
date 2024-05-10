def input_scores():
    num = []
    for i in range(1, 1000):
        n = int(input(f'#{i}? '))
        if n >= 0:
            num.append(n)
        else:
            break
        
    return num

def get_average(lst):
    sum_n = 0
    for j in lst:
        sum_n += lst[j]

    average = j/len(lst)

    return average
        

def show_scores(p):
    for k in range(0,len(p)):
        print(p[k])
    
print('[점수 출력]')
list_score = input_scores()

average = get_average(list_score)

print(f'개인점수:{show_scores(list_score)}')
print(f'평균:{average}')

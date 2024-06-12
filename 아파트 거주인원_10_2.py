def input_num_of_population():
    nPeople = []    
    for f in range(1, 6):
        n = int(input(f'{f}층의 거주인원수는? '))
        nPeople.append(n)

    return nPeople

def show_num_of_population(p):
    cnt = len(p)
    for i in range(cnt) :
        print(f'{i + 1}층의 거주인원수는 {p[i]}명입니다.')

def get_total(lst):
    total = 0
    for n in lst:
        total += n
    
    return total

population = input_num_of_population()

show_num_of_population(population)

# 내장 함수 sum()
total = sum(population) # get_total 함수와 동일한 작동, 리스트의 총합을 구함

print(f'총 거주인원수는 {total}명입니다.')

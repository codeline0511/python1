def find_max(lst):
    m = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > m:
            m = lst[i]
            
    return m

nums = []

for i in range(5):
    n = int(input('정수 입력: '))
    nums.append(n)

# print(f'가장 큰 정수는 {max(nums)}입니다.') --> max() find_max 함수와 같은 역할 
print(f'가장 큰 정수는 {find_max(nums)}입니다.')

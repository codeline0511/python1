def find_max():
    num = []
    for i in range(0, 5):
        n = int(input('정수 입력:'))
        num.append(n)
        value = num[0]
        if i > 0: # 리스트 인덱싱을 통해 최대값 구하기
            if num[i] >= num[i-1]:
                if value <= num[i]:
                    value = num[i]
            else:
                if value <= num[i-1]:
                    value = num[i-1]

    return value

max_num = find_max()
# max_value = max(max_num) 위의 최대값 구하는 부분 제거시 활성화 
print(f'가장 큰 정수는 {max_num} 입니다.')


# 코드1
nums = [11, 22, 33]

n = len(nums) # 리스트 nums의 요소 개수가 저장됌
print(f'요소 개수:{n}개')

nums.append(55) # 맨 마지막 요소로 추가
print(nums)

nums.insert(3, 44) # 3번 요소 자리에 삽입, 자리에서 밀려난 요소는 오른쪽으로 이동 
print(nums)

nums.insert(-1, 50) # 마지막(-1번) 요소 자리에 삽입
print(nums)

del nums[1] # 1번 요소인 22 삭제
print(nums)

del nums[2:4] # 2번부터 4번 전(3번)까지의 요소 [44, 50] 삭제
print(nums)

nums.remove(33) # 시작에서 처음 만나는 33 삭제 
print(nums,'\n')

# 코드2
nums_1 = [11, 22, 33, 44, 55]

nums_1[1:4] = [] # 1번~3번 요소 삭제
print(nums)

nums.clear() # 모든 요소 삭제
print(nums, '\n')

nums_2 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

print(nums_2.index(1)) # 리스트 내에 인수값과 일치하는 첫 번째 요소의 인덱스(자리) 반환
print(nums_2.count(1), '\n') # 리스트 내에 인수값과 일치하는 요소의 개수 반환
# nums_2.index(10) --> 메서드의 인수로 전달된 값이 리스트 내에 존재하지 않는 경우 valueError 오류 발생


nums_3 = [11, 22, 33, 44, 55]
print(22 in nums)
print(66 not in nums)

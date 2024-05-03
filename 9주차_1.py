# 코드1
list1 = [11, 22, 33, 44, 55]
list2 = ['단출하게', '단아하게', '당당하게']
list3 = []
print(list1)
print(list2)
print(list3, '\n')

# 코드2
list4 = [11, '홍길동', 19, 180.5, [10, 20, 30]]
print(list4)
print(list4[1],'님의 키는', list4[-2], 'cm입니다.\n')

# 코드3
sub_list = list1[1:3] # 시작 점 생략:0부터 저장/끝 점 생략:끝까지 저장
print(sub_list) # 22, 33 slicing
print(sub_list[0],'\n') # 22가 출력 

# 코드4
nums = [11, 22, 33, 44, 55]

nums[0] = -1
print(nums)

nums[1:3] = [100, 200, 300] # nums[1:2]까지의 값을 변경!
print(nums)

nums[1] = [100, 200, 300] # 현재의 nums[1]의 값을 변경!
print(nums, '\n')

# 코드5
nums1 = [11, 22, 33]
num2 = []

# nums2 = nums1 ----> 같은 객체에 대한 아이디를 갖음 
nums2 = nums1[:] # -> 변수가 가리키는 리스트 객체의 복사본 생성 

nums2[0] = 0
print(nums1)
print(nums2, '\n')

# 코드6
nums1 = [11, 22, 33]

nums2 = nums1[:]
print(nums1 == nums2)

nums2[1] = 0 # [11, 0, 33]
print(nums1 == nums2)
print(nums1 < nums2)
print(nums1 > nums2, '\n')

# 코드7
nums1 = [11, 22, 33]
nums2 = [44, 55]

nums3 = nums1 + nums2 # 리스트끼리 연결
print(nums3)

nums4 = nums1 * 2 # 리스트의 반복 
print(nums4)

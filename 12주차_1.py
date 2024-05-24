# 코드1
file = open('example.txt', 'w')  # 'w':write 'r':read,
                                 # direc/file 시 지정된 경로의 파일 확인
file.close()
print('파일 열고 닫기 완료')

# 코드2
import os

filename = 'example.txt'         # 파일/디렉터리의 존재 여부 검사
if os.path.exists(filename):
    file = open(filename, 'r')
    file.close()
    print('\n파일 열고 닫기 완료')
else:
    print(f'\nERROR: {filename}이 존재하지 않습니다!')

print('끝')

# 코드3
# import os
if not(os.path.isdir('data')):   # 디렉터리 생성
    os.makedirs('data')

# 코드4
with open('data/example.txt', 'w') as file:
    pass                         # 파일객체를 가지고 파일 입출력 처리 

print('\n파일 열고 닫기 완료')

# file = open(text 이름, 'w') 'w':write 'r':read
# file.close() -> 파일 닫기
#
# import os
#
# if os.path.exists(파일이름): -> 파일/디렉터리의 존재 여부 검사
#   
# if not(os.path.isdir(파일이름)): -> 디렉터리 생성
#     os.makedirs(파일이름)
# 
# with open(디렉터리/파일이름, 'w') as file -> 파일객체를 가지고 파일 입출력 처
#     file.write(넣고 싶은 내용) -> 텍스트 파일에 문자열 저장
#
#     변수 = file.read() -> 전체 내용을 하나의 문자열로 반환
#   
#     lines = file.readlines() -> 각 행 요소에 개행문자가 포함됌

lines = []
with open('data/example.txt', 'r') as file:
    while True:
        line = file.readline()

        if line == '':
            break

        lines.append(line.strip())  # <-문자열 line 앞뒤의 공백문자 제거 후 리스트 lines에 추가

print()
print(lines)
#-------------------------------------------------------
lines = []
with open('data/example.txt', 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

print()
print(lines)


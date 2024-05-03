# 코드1
d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}
print(d)
print(d['python'], '\n') # 딕셔너리는 인덱스가 아닌 키 값으로 설정됌 
# print(d[0]) --> 0이란 키로 저장된 데이터는 없으므로 오류 발생

print(d.get('python'))

res = d.get(0) # 반환되는 값이 없음 
print(res)

# 코드2
d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

key = input('키 입력: ')
if key in d:
    print(d[key])
else:
    print(f'\n오류: 유효하지 않은 키 {key}')

d['Java'] = '자바' # 요소 추가, int형 또는 float형으로 추가 가능, 키 값도 설정 가능
print(d)
d['python'] = 'Python' # 요소 수정, int형 또는 float형으로 수정 가능 
print(d)
del d['programming'] # 요소 삭제 
print(d)
d.clear() # 요소 전부 삭제
print(d) 
d[1] = 1
print(d)

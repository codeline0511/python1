def input_list(lst):
    name = input('이름? ')
    num = input('번호? ')

    lst.append(name)
    lst.append(num)

userinfo = []
input_list(userinfo)
print(f'{userinfo[1]}번 {userinfo[0]}\n')
#-----------------------------------------------------------
msgs = ['단출하게', '단아하게', '당당하게']
for el in range(len(msgs)):
    print(f'{msgs[el]}/', end= '')

print('\n')
msgs = ['단출하게', '단아하게', '당당하게']
for i in range(len(msgs)-1, -1, -1):
    print(f'{msgs[i]}/', end= '')
#-----------------------------------------------------------
scores = [
    ['이찬수', 173, 73],  # 리스트 여러번 중첩 가능, 하지만 가독성은 떨어짐
    ['홍길동', 169, 65]
]

print(scores)
print(scores[0])
print(scores[0][0])
print()
#-----------------------------------------------------------
d = {
    'python':'파이썬',
    'basic':'기초',
    'programming':'프로그래밍'
}

for key in d.keys():
    print(key, d[key])

#-----------------------------------------------------------
def dict_get(dic, key):  # 딕셔너리의 키 값 찾기
    if key in dic:
        return dic[key]
    else:
        return None

d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

res = dict_get(d, 'python')
if res != None:
    print(res)
else:
    print('오류: 잘못된 키')

res = dict_get(d, 0)
if res != None:
    print(res)
else:
    print('오류: 잘못된 키')

print()

def dict_append(dic, key, value):     # 딕셔너리의 키 값 추가
    if key in dic:
        return False

    dic[key] = value
    return True

d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

if dict_append(d, 'PYTHON', '파이썬'):
    print('추가 성공')
else:
    print('추가 실패')

if dict_append(d, 'basic', '베이직'):  #이미 있는 키 값에 대해서는 추가 불가
    print('두 번째 추가 성공')
else:
    print('두 번째 추가 실패')

print(d)
print()

def dict_delete(dic, key):  # 딕셔너리의 키 값 삭제
    if key in dic:
        del dic[key]
        return True
    else:
        return False

d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}
if dict_delete(d, 'basic'):
    print('삭제 성공')
else:
    print('삭제 실패')

if dict_delete(d, 'deep'):
    print('삭제 성공')
else:
    print('삭제 실패')

print(d)


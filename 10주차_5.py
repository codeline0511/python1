# 코드1
def dict_get(dic, key):
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

# 코드2
def dict_append(dic, key, value):
    if key in dic:
        return False

    dic[key] = value
    return True

d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}

if dict_append(d, 'PYTHON', '파이썬'):
    print('추가 성공')
else:
    print('추가 실패')

if dict_append(d, 'basic', '베이직'):
    print('두 번째 추가 성공')
else:
    print('두 번째 추가 실패')

print(d)
print()

# 코드3
def dict_delete(dic, key):
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

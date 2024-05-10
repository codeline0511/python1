# 코드1
def input_list(lst):
    name = input('이름? ')
    num = input('번호? ')

    lst.append(name)
    lst.append(num)

userinfo = []
input_list(userinfo)
print(f'{userinfo[1]}번 {userinfo[0]}\n')

# 코드2
def input_list(lst): #위의 코드와 동일하게 작동, 효율성은 높음 
    name = input('이름? ')
    num = input('번호? ')

    lst = []
    lst.append(name)
    lst.append(num)
    return lst     # 리스트 반환 

input_list(userinfo)
print(f'{userinfo[1]}번 {userinfo[0]}\n')


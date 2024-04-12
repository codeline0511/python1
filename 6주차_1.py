# 코드1
n1 = int(input('첫 번째 정수는?'))
n2 = int(input('두 번째 정수는?'))

print(f'{n1}은/는 {n2} 보다 큽니까? {n1 > n2}')
print(f'{n1}은/는 {n2} 보다 크거나 혹은 같습니까? {n1 >= n2}')
print(f'{n1}은/는 {n2} 보다 작습니까? {n1 < n2}')
print(f'{n1}은/는 {n2} 보다 작거나 혹은 같습니까? {n1 <= n2}')
print(f'{n1}은/는 {n2} 와 같습니까? {n1 == n2}')
print(f'{n1}은/는 {n2} 와 다릅니까? {n1 != n2}\n')

# 코드2
string1 = 'abc'
string2 = 'aaa'

print(f'{string1}은/는 {string2} 보다 길이가 깁니까? {string1 > string2}')
print(f'{string1}은/는 {string2} 보다 길이가 같거나 깁니까? {string1 >= string2}')
print(f'{string1}은/는 {string2} 보다 길이가 짧습니까? {string1 < string2}')
print(f'{string1}은/는 {string2} 보다 길이가 같거나 짧습니니까? {string1 <= string2}')
print(f'{string1}은/는 {string2} 와 같습니까? {string1 == string2}')
print(f'{string1}은/는 {string2} 와 다릅니까? {string1 != string2}\n')

# 코드3
age = int(input('당신의 나이는 몇 살입니까?'))

res = age >= 0 and age <= 120 # 0 ~ 120
print(f'{age}은(는) 유효한 나이인가? {res}')

res = age < 0 or age > 120 # ~ -1, 121 ~
print(f'{age}은(는) 유효한 나이가 아닌가? {res}')
print(f'{age}은(는) 유효한 나이인가? {not res}\n')


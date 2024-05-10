# 코드1
msgs = ['단출하게', '단아하게', '당당하게']
for e in msgs:
    print(f'{e}/', end= '')

# 코드2
print('\n')
msgs = ['단출하게', '단아하게', '당당하게']
for el in range(len(msgs)):
    print(f'{msgs[el]}/', end= '')

# 코드3
print('\n')
msgs = ['단출하게', '단아하게', '당당하게']
for i in range(len(msgs)-1, -1, -1):
    print(f'{msgs[i]}/', end= '')

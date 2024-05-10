# 코드1
scores = [
    ['이찬수', 173, 73],
    ['홍길동', 169, 65]
]

print(scores)
print(scores[0])
print(scores[0][0])
print()

for g in scores:
    for e in g:
        print(e, end='/')
    print()

print()
for gi in range(len(scores)):
    for ei in range(len(scores[gi])):
        print(scores[gi][ei], end='/')
    print()

# 질문? --> 리스트는 몇번이나 중첩이 가능하다!
print()
list_3 = [ [ ['a', 'A'], 'b', 'B'], 'c', 'C' ]


print(list_3)
print(list_3[0])
print(list_3[0][0])
print(list_3[0][0][0])

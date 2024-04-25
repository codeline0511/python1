def degree_integer(n, m):
    if (n+m) >= 0:
        return n+m
    if (n+m) < 0:
        return -(n+m)

while True:
    a = int(input('수1 입력:'))
    b = int(input('수2 입력:'))

    result = degree_integer(a,b)
    print(f'|{a} + {b}| = {result}')

    cont = input("계속하시겠습니까?")
    print()
    if cont != 'Y'and cont != 'y':
        break

def boolean_front_number(n, binary):
    print(n, '을(를)', binary,'만큼의 비트를 이동시키셨습니다.')
    a = n << binary
    return a

def boolean_back_number(n, binary):
    print(n, '을(를)', binary,'만큼의 비트를 이동시키셨습니다.')
    a = n >> binary
    return a

def boolean_only_one(n):
    print(n, '비트가 나타내는', n, '개의 1들') 
    a = bin((1 << n) - 1)
    return a


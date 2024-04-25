def set_all_bits(n):
    m = (1 << n) - 1
    return m

def get_integer(promt):
    message = int(input(promt))
    return message

bit = get_integer('설정할 비트 수는?')
result = set_all_bits(bit)
print(f'{bit} 비트를 모두 1로 설정한 수는 {result} ({bin(result)}) 이다.')

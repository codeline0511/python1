#코드 1
msg = '안녕하세요' # 0 1 2 3 4 / -5 -4 -3 -2 -1
print(msg[0]) # == msg[-5]
print(msg[-1]) # == msg[4]
print(msg[2:4]) # a:b == a <= x < b
print(msg[:2]) # 0 1 --> a: == 0 <= x < a
print(msg[2:]) # 2 3 4 --> :a == a <= x < n (n = 문자의 갯수)

#코드 2
print('\n안녕''하세요') #문자열 리터럴의 경우에만 사용 가능 
print('안녕' + '하세요')

msg1, msg2 = '안녕', '하세요'
print(msg1 + msg2)
print('안녕' + msg2)
print(msg1, '+', msg2)

res = 2 * 2
print('\n2 * 2 = ' + str(res)) #문자열은 다른 자료형과 연결 지원 하지 않음
print('!' * 5) #3500번 금지, 50줄 이상 출력되는 4000번 이상은 squeeze함 
print(5 * '?')


# 코드1 사용자 정의 함수를 사용 
def do_one_set(n): # pass?
  for cnt in range(1, n + 1):
      print(cnt, end = ' ')
  print()

for s in range(3):
    do_one_set(15)

# 코드2 -함수를 구성하는 문장들을 직접 기술
for s in range(3):
    n = 15
    for cnt in range(1, n+1):
        print(cnt, end = ' ')
    print()

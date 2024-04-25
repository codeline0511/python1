print('첫 번째"아해"가"도로"로 달리오') # 두 종류의 따옴표는 한번만 중복
print("두 번째'아해가\"도로\"로 질주하다'흔적도 사라졌소.") # \" \'를 쓰면 여러번 중복 가능
print("세 번째\t아해는...\n어디로 갔는지 모르겠소") # \t는 일정 칸 띄우기(=tab), \n은 줄바꿈
print("네 번째\\아해\\는 가다가...\
아, 논두렁에 빠졌소.") # \\ 는 \ 출력, \만 하면 다음 줄에 작성 가능

n = 'Orin ayo'
m = '&Monocrome'

length = len(n)
print('\n',length)
print(n[0:3])
print(n[1:])
print(n[:4]) # 띄어쓰기된 공간도 포함
print(n[-2:]) # -는 거꾸로 시작, -1부터 시작
print(n[-7:-2])
print(n + m)
print(n[2:]+m[-2:]) # 슬라이싱한 문자열도 합 가능
print((n + m)[3:11]) # 두 문자열을 합친 다음 슬라이싱도 가능

res = 2 * 2
#print('2 * 2=' + res) # res는 string형이 아닌 int형
print('\n2 * 2=',res) # 반점으로 구별, 붙여쓰질 못함 
print('2 * 2='+str(res)) # str로 string 전환
print(f'2 * 2= {res}') # f-문자열로 문자열 형식화
print('-' * 20) # 문자열은 곱도 가능 

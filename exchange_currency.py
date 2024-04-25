exchange_rate = 0

def set_rate(rate):
    global exchange_rate #exchange_rate라는 변수가 전역변수임을 선언 
    exchange_rate = rate

def get_rate():
    return exchange_rate

def to_dollar(won):
     return won / exchange_rate
    
def to_won(dollar):
    return dollar * exchange_rate

def main():
    print("###환율 변환 모듈 테스트###")
    set_rate(1010)
    print('오늘의 환율', get_rate()) #set_rate(1010)과 동일 
    print(to_won(2), '원 =', to_dollar(2020),'달러')
    print(to_dollar(2020), '달러 =', to_won(2), '원')

if __name__=='__main__':
    main()

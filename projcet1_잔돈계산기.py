def exchange(n, m):
    a = m - n

    m10000 = a // 10000
    ex = a % 10000
    
    m5000 = ex // 5000
    ex_1 = ex % 5000
    
    m1000 = ex_1 // 1000
    ex_2 = ex_1 % 1000

    m500 = ex_2 // 500
    ex_3 = ex_2 % 500

    m100 = ex_3 // 100
    ex_4 = ex_3 % 100

    m50 = ex_4 // 50
    ex_5 = ex_4 % 50
    
    m10 = ex_5 // 10

    print(f'잔돈: {a}원')
    print(f'> 10000원 권 {m10000} 장')
    print(f'> 5000원 권 {m5000} 장')
    print(f'> 1000원 권 {m1000} 장')
    print(f'> 500원 짜리 {m500} 개')
    print(f'> 100원 짜리 {m100} 개')
    print(f'> 50원 짜리 {m50} 개')
    print(f'> 10원 짜리 {m10} 개')

buy = int(input('구매한 물건의 총구매 금액은?'))
money = int(input('고객으로부터 지불받은 금액은?'))
exchange(buy, money)

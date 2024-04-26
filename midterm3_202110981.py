def exchange(money):
    exchange_rate = float(input('오늘의 환율은(100엔)? '))

    n1 = int(money // (exchange_rate * 100))
    exchange1 = (money % (exchange_rate * 100))
    print(f'10000엔의 개수: {n1}')

    n2 = int(exchange1 // (exchange_rate * 50))
    exchange2 = (exchange1 % (exchange_rate * 50))
    print(f'5000엔의 개수: {n2}')

    n3 = int(exchange2 // (exchange_rate * 10))
    exchange3 = (exchange2 % (exchange_rate * 10))
    print(f'1000엔의 개수: {n3}')

    n4 = int((exchange3 // 10) * 10)
    print(f'잔돈: {n4}원')
    
money_won = int(input('엔화지폐로 교환하고자 하는 금액은? '))                     
exchange(money_won)
 

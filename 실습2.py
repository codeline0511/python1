import os

filename = 'shopping.txt'
if os.path.exists(filename):
    print('[파일 읽기]')
    print()
    print(f'\n>>> 장바구니 보기:{shopping_bag}')
    
    while True:
        item = input('상품명? ')
        if item == '' or item == ' ':
            break
        else :
            print(f'장바구니에 {item}가(이) 담겼습니다.\n')
            shopping_bag.append(item)
            print(f'\n>>> 장바구니 보기:{shopping_bag}')

        with open('shopping.txt', 'w') as file:
            file.write(shopping_bag)
            break
else:
    shopping_bag = []
    while True:
        item = input('상품명? ')
        if item == '' or item == ' ':
            break
        else :
            print(f'장바구니에 {item}가(이) 담겼습니다.\n')
            shopping_bag.append(item)

        print(f'\n>>> 장바구니 보기:{shopping_bag}')

        with open('shopping.txt', 'w') as file:
            file.write(shopping_bag)


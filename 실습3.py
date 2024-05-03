shopping_bag = []
while True:
    item = input('상품명? ')
    if item == '' or item == ' ':
        break
    else :
        print(f'장바구니에 {item}가(이) 담겼습니다.\n')
        shopping_bag.append(item)

print(f'\n>>> 장바구니 보기:{shopping_bag}')


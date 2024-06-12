import os

filename = 'shoppingbag.txt'

def buy(sbag):
    print('[구입]')
    sbag = input('상품명?')
    if sbag == '' or sbag == ' ':
        return False
    else:
        print(f'장바구니에 {sbag}가(이) 담겼습니다.\n')
        shopping_bag.append(sbag)

def show(sbag):
    print(f'>>> 장바구니 보기:{shopping_bag}')

def save_data(sbag, filepath):
    with open(filepath, 'w') as file:
        for item in sbag:
            file.write(f'{item}\n')

def load_data(filepath):
    lines = []
    with open(filepath, 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))
    return lines

if os.path.exists(filename):
    print('[파일 읽기]\n')
    shopping_bag = load_data(filename)
    show(shopping_bag)

else:
    shopping_bag = []
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
save_data(shopping_bag, filename)

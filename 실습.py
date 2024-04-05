def divide_name(name): #띄어쓰기 시 공백도 문자열에 포함되니 주의
    last_name = name[0]
    first_name = name[1:]
    print('-' * 10,'\n')
    print('성:\t', last_name)
    print('이름:\t', first_name, '\n')
    print('-' * 10)
    

a = input('당신의 이름은? ')

divide_name(a)

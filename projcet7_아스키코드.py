def find_char_type(char):
    if char >= 'A' and char <= 'z':
        print('알파벳 문자를 입력했습니다.')
        
    elif char >= '0' and char <= '9':
        print('숫자 문자를 입력했습니다.')
        
    elif char == ' ' or char == '':
        print('공백 문자를 입력했습니다.')
        
    else :
        print('기타 문자를 입력했습니다.')

while True:
    char = input('한 문자 입력?')
    find_char_type(char)
    cont = input('계속하시겠습니까?')
    
    if cont != 'Y' and cont != 'y':
        break
    
    else:
        print()

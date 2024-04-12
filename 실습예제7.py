def find_char_type(ch):
    if ch == ' ':
        return '공백'
    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        return '알파벳'
    elif '0' <= ch <= '9':
        return '숫자'
    else :
        return '기타'

c = input('한 문자 입력?')
ctype = find_char_type(c)
print(f'{ctype} 문자를 입력했습니다.')

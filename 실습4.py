from 실습3 import rep_char as Rc

def draw_line_string(string):
    char = '-'
    length = len(string) * 2 + 4
    Rc(char, length)
    print(f'  {string}  ')
    Rc(char, length)
    
    

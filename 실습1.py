import os

with open('readme.txt', 'w') as file:
    file.write('안녕하세요, 반갑습니다.')
    file.write('\n이 파일은 테스트 파일 저장을 위해 작성된 텍스트 문서입니다.')
    file.write('\n조금 낯설더라도 포기하지 마세요.')

def show_file(filename):
    with open(filename, 'r') as file:
        i = 1
        while True:
            line = file.readline()
            if line == '':
                break
            print(f'{i}: {line.strip()}')
            i += 1

fn = input('파일명: ')
show_file(fn)

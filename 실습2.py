def introduce(name, grade):
    last_name = name[1:]
    up_grade = grade + 1
    return f'{last_name}은 내년에 {up_grade}학년입니다.'

a = input('이름?')
b = int(input('학년?'))
result = introduce(a, b)
print(result)

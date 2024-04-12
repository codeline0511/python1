score = int(input('점수는?'))

if score >= 90 :
    grade = 'A'
    print(f'{score}점이므로 {grade}', end = '')
elif score >= 80 :
    grade = 'B'
    print(f'{score}점이므로 {grade}', end = '')
elif score >= 70 :
    grade = 'C'
    print(f'{score}점이므로 {grade}', end = '')
elif score >= 60 :
    grade = 'D'
    print(f'{score}점이므로 {grade}', end = '')
else :
    grade = 'F'
    print(f'{score}점이므로 {grade}', end = '')
print('학점입니다.')


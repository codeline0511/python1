from datetime import datetime
import os
import pickle

filename = 'last.dat'

class Time:
    def __init__(self, hour = 0, minute = 0):
        self.__hour = hour
        self.__minute = minute

    def __str__(self):
        return f'{self.__hour:02}:{self.__minute:02}'

#        
def get_current_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return Time(hour, minute)

def save_time(time):
    with open(filename, 'wb') as file:
        pickle.dump(time, file)

def load_time():
    with open(filename, 'rb') as file:
        t = pickle.load(file)
    return t

#
if os.path.exists(filename):
    t = load_time()
    print(f'안녕하세요, 마지막으로 {t}에 실행되었습니다.')
else:
    print('안녕하세요, 처음 실행되었습니다.')

t = get_current_time()
print(f'지금은 {t} 입니다.')
save_time(t)

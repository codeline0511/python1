from datetime import datetime
now = datetime.now
hour = now.hour
minute = now.minute

class Time:
    def __init__(self, hour = 0, minute = 0):
        self.__hour = hour
        self.__minute = minute

    def display(self):
        print(f'{self.__hour:02d}:{self.__,minute:02d}')


def main():
    pass

if __name__ == '__main__':
    main()

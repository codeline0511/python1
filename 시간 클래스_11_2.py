class Time:
    def __init__(self, hour = 0, minute = 0):
        self.__hour = hour
        self.__minute = minute

    def display(self):
        print(f'{self.__hour:02d}:{self.__minute:02d}')

    def add(self, time):
        h = self.__hour + time.__hour
        m = self.__minute + time.__minute
        if m >= 60:
            h += 1
            m -= 60
        return Time(h, m)

    @staticmethod
    def is_valid(hour, minute):
        if 0 <= hour < 24 and 0 <= minute < 60:
            return True
        return False


def main():
    t1 = Time(9)
    t2 = Time(9, 30)

    t1.display()
    t2.display()

    later = t1.add(Time(1, 15))
    later.display()

    if Time.is_valid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')

if __name__ == '__main__':
    main()

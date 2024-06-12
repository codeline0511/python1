class Point:  # 클래스 설정 
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self, x, y): # 필요시 x, y의 유효성을 확인
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)

def test():  # 함수 정의 
    p1 = Point()
    p2 = Point(2, 3)

    p1.show();

    p1.set(10, 20); p1.show();

    p2.show();

    x, y = p2.get()
    print(f'x={x}, y={y}')

if __name__ == '__main__':
    test()

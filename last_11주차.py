# class 아무개:
#     def __init__(self):  주 함수에서 접근하려는 시도를 막음
#
#     def __관련 정의(self):
# 원하는 객체 = class의 이름()

class Circle:
    def __init__(self, radius):  
        self.__radius = radius 
        
    def getCircumference(self):   
        result = 2 * 3.14159265 * self.__radius    
        return result

    def getArea(self):
        result = 3.14159265 * self.__radius ** 2   
        return result

    def setRadius(self, radius):  # 액세스 메서드 사용
        if radius <= 0:           # 보다 나은 세터 구현 
            return False
        
        self.__radius = radius
        return True

    def getRadius(self):
        return self.__radius

big = Circle(10)
big.setRadius(-2)  
print(big.getRadius())
big.setRadius(20)  
print(big.getRadius())
print()

class Circle:
    __PI = 3.14159265  # 클래스 변수를 갖는 클래스 정의
    
    def __init__(self, radius):  # 외부에서의 변수 접근 차단
        # self.__PI = 3.14159265 / 이러면 객체가 비효율적으로 공통의 정보를 갖게 됌
        self.radius = radius
        
    def getCircumference(self):   
        result = 2 * self.__PI * self.radius   
        return result

    def getArea(self):
        result = self.__PI * self.radius ** 2
        return result
    
    @staticmethod  
    def getPI():
        return Circle.__PI

small = Circle(1)   
big = Circle(10)    

print(f'반지름 {small.radius}인 원의 ', end='')
print(f'둘레는 {small.getCircumference():.2f}이고, ', end='')
print(f'넓이는 {small.getArea():.2f}이다.')

print(f'반지름 {big.radius}인 원의 ', end='')
print(f'둘레는 {big.getCircumference():.2f}이고, ', end='')
print(f'넓이는 {big.getArea():.2f}이다.')

import math
print(f'\nPI의 값:{math.pi}')


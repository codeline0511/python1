import pickle

filepath = 'data/circle.bin'

class Circle:
    __PI = 3.14159265

    def getPI(self):
        return __PI

    def __init__(self, radius):
        self.__radius = radius

    def getCircumference(self):
        result = 2 * Circle.__PI * self.__radius
        return result

    def getArea(self):
        result = Circle.__PI * self.__radius ** 2
        return result

with open(filepath, 'wb') as file:
    c1 = Circle(10)
    pickle.dump(c1, file)

with open(filepath, 'rb') as file:
    c2 = pickle.load(file)
    print(f'원의 넓이는 {c2.getArea()}')

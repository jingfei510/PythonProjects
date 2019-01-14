class Triangle:
    # 三角形长宽，面积
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2
        return area


class Square(Triangle):
    # 正方形边长，面积
    def __init__(self, size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area


def fanc(its):
    area = its.getArea()
    print("面积为" + str(area))


a = Triangle(5, 5)
# print(a.getArea())
b = Square(5)
# print(b.getArea())

# 不同对象调用同一个函数，出现不同结果就是多态。
fanc(a)
fanc(b)

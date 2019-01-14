class Turtle():
    def __init__(self, x):
        self.num = x


class Fish():
    def __init__(self, y):
        self.num = y


class Pool():
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("乌龟%d只！ 鱼%d条！" % (self.turtle.num, self.fish.num))


p = Pool(3, 5)

p.print_num()

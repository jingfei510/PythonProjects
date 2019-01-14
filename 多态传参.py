class A:
    def fanc(self, x, y):
        print(x + y)


class B:
    def fanc(self, x, y):
        return x + y


c = A()
c.fanc(1, 2)
c.fanc("hello", "world")

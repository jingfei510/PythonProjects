class A:
    def __init__(self):
        print("enter A")
        print("leave A")
        
class E:
    def __init__(self):
        print("enter E")
        print("leave E")
        self.fanc()
    def fanc(self):
        print("我是fanc")

class B(A):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")


class C(E):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")

class D(B,C):
    def __init__(self):
        print("enter D")
        super(D,self).__init__()
        
        print("leave D")

d=D()

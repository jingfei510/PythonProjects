class A:
    def __init__(self):
        print("enter A")
        print("leave A")

class B(A):
    def __init__(self):
        print("enter B")
        A.__init__(self)
        print("leave B")

class C(A):
    def __init__(self):
        print("enter C")
        A.__init__(self)
        print("leave C")

class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("leave D")

d=D()

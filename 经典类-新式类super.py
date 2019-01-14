class A:
    def __init__(self):
        print("enter A")
        print("leave A")

class B(A):
    def __init__(self):
        print("enter B")
        super().__init__()
        print("leave B")

class C(A):
    def __init__(self):
        print("enter C")
        super().__init__()
        print("leave C")

class D(B,C):
    def __init__(self):
        print("enter D")
        B.__init__(self)
        C.__init__(self)
        print("leave D")

d=D()

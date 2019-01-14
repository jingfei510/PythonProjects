import random as r
class Fish():
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move (self):
        self.x-=1
        print("这是我现在的位置：", self.x,self.y)
class GoldFish(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):#重写父类的方法
        #Fish.__init__(self)#调用父类的方法1
        super().__init__()#用super()函数，调用父类的方法2
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("我好饿！")
            self.hungry=False
        else:
            print("我吃饱了！")
            

class Father:
    money = 1000000
    __money = 100000000   #私房钱
    def drive(self):
        print("i can drive a car!")

class Mother:
    money = 10000
    def work(self):
        print("我是一个it人员")
        
class Son(Father,Mother):   #继承人两个人同一个属性时，只继承第一个人的。

    def drive(self):
        print('i can drive a tank!')  #方法重载
        Father.drive(self)

    #pass   #没有下面代码的时候，写pass继承全部
    def pay(self):
        print(self.money)
        #print(self.__money)# 不能花私房钱
        
tom = Father()
print(tom.money)
tom.drive()

print('#'*30)
jerry = Son()
print(jerry.money)
jerry.drive()
jerry.pay()
jerry.work()

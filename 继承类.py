# 真爸爸--穷class trueFather:
class TrueFather:
    money = 1000
    __privateMoney = 0

    def fanc(self):
        print('虽然没钱，但我会开汽车！')


# 假爸爸---有钱有银行
class PhonyFather:
    money = 1000000
    __privateMoney = "a bank"  # 私有属性，有银行，不能直接访问

    def fanc(self):
        print("不但有钱，还会开飞机！")

    def present(self):
        # 假爸爸看到真爸爸太穷了，就给了他10000元
        TrueFather.money += 10000
        return TrueFather.money

    def getPrivate(self):
        return self.__privateMoney


class Son(TrueFather, PhonyFather):
    # Son继承了两个爸爸，但是如果两个爸爸中的属性相同，他只能继承左边第一个父类，不能继承右边的父类.
    # 但如果两个父类的属性不同，就可以全部继承
    def fanc(self):
        # 覆写属性
        print("我还小，不让开汽车，也不让开飞机！")


bob = Son()  # 实例化Son对象bob
print("我继承的钱：")
print(bob.money)  # 因为两个父类的monoy属性相同所以只继承第一个爸爸的钱

print("因为太少了，不够花，我问假爸爸要了点，总共：")
print(bob.present())  # 因为第一个父类没有present属性，所以继承第二个父类（假爸爸），查看继承的假爸爸的属性
bob.fanc()  # 调用覆写的属性
print("*" * 50)
# __privateMoney   #私有属性不能访问，想访问有两种方法
# 方法一：不用调用函数。
father = TrueFather()  # 实例化真父类
print("真爸爸的私有钱财：")
print(father._TrueFather__privateMoney)
print("*" * 50)
# 方法二：写方法getPrivate,调用函数查看假爸爸的私有属性
print("假爸爸的私有钱财:")
print(bob.getPrivate())

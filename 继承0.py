class Father:
    money = '1000000'

    def drive(self):
        print('i am a dirver')

class Son(Father):
    def drive(self):
        print("i am a baobao")#方法重写

tom = Father()
print(tom.money)
tom.drive()

print('---'*10)

jerry = Son()
print(jerry.money)
jerry.drive()

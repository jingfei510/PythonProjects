class Human:
    name = ' '
    money = ' '

    def __init__(self,name,money):
        print("#"*30)
        #print(zhangsan.name)   #访问错误。
        print(self.name)     #直接执行，类中名字为空，所以运行为空


        self.name = name    
        self.money = money  #把参数中的值money赋值给自己的参数money.self

zhangsan = Human('zhangsan',10000)
#zhangsan.name = 'laowang'
print(zhangsan.name)
print(zhangsan.money) #调用赋值后的值。可以改变类中的原始值。
#print(self.name)    #访问错误。函数内部用self，外部用名字
print(Human.name)   #访问类

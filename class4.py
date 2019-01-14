class Human:
    name = 'ren'
    gender = 'male'
    age = '25'
    __money = 10000   #私有属性

    def __init__(self):
        print('#'*30)  #可以直接执行，初始化作用

    

    def say(self):
        print('私有属性i have%d yuan'%self.__money)  #内置函数访问私有属性
        self.__lie()    #内部调用私有属性，直接调用__lie不行
    def __lie(self):
        print('i was %s'%self.name)
        self.name = 'laowang'
        print('now i am %s'% self.name)
        print(Human.name)
        print(zhangsan.name)
        
    
zhangsan = Human()
zhangsan.name  = 'zhangsan'
print(zhangsan.name)
zhangsan.say()
#zhangsan.lie()
#print(zhangsan.__money)   #访问不到私有属性

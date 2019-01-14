class Human:
    '''
this is Human class docsyring!!
    '''
    name = 'ren'
    gender = 'male'
    age = '25'
    __money = 8000  #私有属性

    def __init__(self,name,age):   #初始化的作用，自动调用。
        print("#"*30)
        self.name = name
        self.age = age
        print("#"*30)

    def  __str__(self):
        msg = 'hi ! i am the object'
        return msg

        
    def say(self):
        print("my name is %s ,i have %d"%(self.name,self.__money))
        self.__lie()   #私有属性只能内部调用
        
    def __lie(self):
        print('i have 5000')

    
        
zhangsan = Human('zhangsan',30)
#zhangsan.name = 'zhangsan'
#print(self.__lie)调用不出来
#print(zhangsan.name,zhangsan.age)
#zhangsan.say()
print(zhangsan)  #msg人性化
print(Human.age)
print(Human)   #下方是人性化
print(Human.__doc__)  #注释类




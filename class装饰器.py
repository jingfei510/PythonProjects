class human:
    
    name = 'name'
    age = '25'
    __money=8000

    def __init__(self,name,age):
        print("#"*50)
        self.name=name
        self.age=age
        print("*"*50)
        
    @property
    #@classmethod   #有self，用装饰器2  
    def say(self):
        print("%s,,,%d"% (self.name,self.__money))
        return self.name

         
    @staticmethod   #装饰器1
    def bye():
        print("Game over!")
human.bye()
tom = human('name',30)
tom.bye()    #生成对象后调用bye ，需要装饰器1

#print(human.say)   #装饰器2

print(tom.say)



import time

def deco(func):   #装饰器函数
    def wrapper():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT)*1000
        print('it is %f ms'% msecs)
    return wrapper  #吧装饰的函数返回给myfunc


@deco   
def myfunc():
    print('myfunc start....')
    time.sleep(1.5)  #停顿1.5秒
    print('myfunc end....')


print("myfunc is",myfunc.__name__)

   
#myfunc = deco(myfunc)  #相当于'@deco'  #每次运行都加装饰。
print('#'*50)

print("myfunc is",myfunc.__name__)

myfunc()






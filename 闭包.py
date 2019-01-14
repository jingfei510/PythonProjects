def hello_conf(prefix):   #闭包
    def hello(name):
        print(prefix,name)
    return hello
a = hello_conf('Good Morning! ')   #把hello函数返回给a，并且附加上顶级函数的值
a('jf')      #调用hello赋值给a的函数
print(a.__name__)
print(id(a))

b = hello_conf('Good Afternoon!')
b('zhangdanyang')
b(3)
b('1+2+3')
print(b.__name__)
print(id(b))

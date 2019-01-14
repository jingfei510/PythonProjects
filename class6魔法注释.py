class Human:
    '''
this is Human class docstring!!!
    '''
    name = ''
    money = ''

    def __str__(self):

        #<__main__.Human object at 0x03180BD0>
        #魔法发方法初始化。
        msg = 'i am the object!!'
        
        return msg


zhangsan = Human()
#zhangsan.name = 'zhangsan'
print(zhangsan)
print(Human.__doc__)  #内置属性看注释。


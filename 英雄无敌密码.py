'''英雄无敌
'''
import os
welcome = 'welcome to heroes world'
i = 0
while 1:
    if os.path.isfile('lock.log'):#判断输入的是否为之前已经锁上的
        print('clocked')
        break
    username = input('login:')#输入用户名和密码
    password = input('password:')
    i += 1
    if username == 'jf' and password == '123':#判断是否正确
        print(welcome)
    else:
        if i == 3:#判断3次之后锁住
            usermsg = username+'--->'+password
            open('lock.log','w').write(usermsg)
            print('locked by %s'%username)
            break
        continue
    break
    

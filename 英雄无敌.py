'''英雄无敌




'''

'''map = ((0,0),(1,0),(2,0),
       (0,1),(1,1),(2,1),
       (0,2),(1,2),(2,2))
'''
import random  #随机数
welcome = "welcome to lol"
print(welcome)
mapmsg = '######'#地图
map = ['#','#','#','#','#','#','#']#列表设计地图
contrl = '\nd is -> ,a is <-,now you are"*",*#####'
name = input("plaese input your name:")#输入名字
if not name:
    name = "player"#自定义名字
print("congrulation you")
hp = 50
usermsg = {'name':name,'hp':hp}
print("your name:",usermsg['name'],'hp is :',usermsg['hp'])
print(mapmsg,contrl)

def apple(hp):
    hp+=10  #加血
    return hp


def bomb(hp):
    hp-=10  #减血
    return hp

eventlist = [apple,bomb]

point = 0
while 1:
    map[point] = '*'
    print('you are here',"".join(map))
    userinput = input('go or exit\n')
    if userinput == 'd' and  point < 6:
        map[point] = '#'
        point +=1
        usermsg['hp']=random.choice(eventlist)(usermsg['hp'])#从列表eventlist中产生随机数
        print(usermsg['hp'])
    elif userinput == 'a' and point > 0:
        map[point] = '#'
        point -=1
        usermsg['hp']=random.choice(eventlist)(usermsg['hp'])
        print(usermsg['hp'])
    elif userinput == 'exit':
        print("goodbey")
        break
    else:
        print(contrl)
        
""" if point == 3:
        usermsg['hp']=apple(usermsg['hp'])
        print('blood is %s' % (usermsg['hp']))
    if point == 4:
        usermsg['hp']=bomb(usermsg['hp'])
        print('blood is %s' % (usermsg['hp']))
    #不是随机数
"""
   
   
        
        
        







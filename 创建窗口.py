import tkinter
from turtle import *
import turtle
root = tkinter.Tk() #生成主窗口
menu= tkinter.Menu(root)  #生成菜单
submenu=tkinter.Menu(menu,tearoff=0) #生成下拉菜单
submenu1=tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='Open')#添加下拉菜单指令名字
submenu1.add_command(label='F5')
menu.add_cascade(label='File',menu=submenu)#将下拉菜单添加到菜单
menu.add_cascade(label='Run',menu=submenu1)
root.config(menu=menu)  #启用菜单

label = tkinter.Label(root,text='你好')  #生成标签
label.pack()   #将标签添加至主窗口
button1 = tkinter.Button(root,text='我爱你') #生成按钮
button1.pack()





def tx(event):
    pensize(1)
    pencolor('red')
    fillcolor('pink')
    speed(5)
    up()
    goto(-30,100)
    down()
    begin_fill()
    left(90)
    circle(120,180)
    circle(360,70)
    left(38)
    circle(360,70)
    circle(120,180)
    end_fill()
    up()
    goto(-100,-100)
    down()
    write("景飞love张丹杨",font=("Arial",18,"normal"))

button1.bind('<Button-1>',tx)


root.mainloop() #进入消息循环


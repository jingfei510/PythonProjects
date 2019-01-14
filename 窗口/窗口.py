#GUI- tkinter
import tkinter
import turtle
root = tkinter.Tk()

######菜单
menu = tkinter.Menu(root)#生成菜单对象，root生成到窗口中
submenu1 = tkinter.Menu(menu,tearoff = 0)#生成下拉菜单
submenu1.add_command(label = "Open")
submenu1.add_command(label = "Save")
menu.add_cascade(label = "File",menu = submenu1)#在菜单项File里面添加下拉菜单

submenu2 = tkinter.Menu(menu,tearoff = 0)
submenu2.add_command(label = "Cut")
submenu2.add_command(label = "Copy")
menu.add_cascade(label = "Edit",menu = submenu2)

submenu3 = tkinter.Menu(menu,tearoff = 0)
submenu3.add_command(label = "Python Shell")
submenu3.add_command(label = "Check Module")
menu.add_cascade(label = "Run",menu = submenu3)

root.config(menu = menu)#配置
######

######组件
label = tkinter.Label(root,text="hello")#生成标签
label.pack()
button1 = tkinter.Button(root,text = "五角星")#生成按钮
button1.pack()

def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
button1.bind("<Button-1>",wjx)#在按钮上绑定鼠标左键





root.mainloop()

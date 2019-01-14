'''###对象开发
import wx
app = wx.App()
frame = wx.Frame(parent = None)
frame.Show()
app.MainLoop()
###


###
import wx
class MyFrame(wx.Frame):
    frame = wx.Frame(parent = None)
    frame.Show()
###
 '''
###子类化开发
import wx
import turtle
class MyApp(wx.App):
    def OnInit(self):
        #MyFrame()
        frame = wx.Frame(parent = None,
                                       title = "记事本",
                                       size=(400,200),
                                       pos = (800,300))#生成框架窗口
        panel = wx.Panel(frame ,-1)
        
        self.buttonWJX = wx.Button(panel,
                                                       -1,"五角星",
                                                       size = (75,25),
                                                       pos = (10,10))
        
        
        self.buttonMG = wx.Button(panel,
                                                       -1,"玫瑰花",
                                                       size = (75,25),
                                                       pos = (200,300))
        frame.Show()#显示窗口
        return True
        
        


        
        
    def OnButtonWJX(self,event):#必须多写一个参数，作为事件按钮
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)

    def OnButtonMG(self,event):
        turtle.speed(10.4)
        turtle.penup()
        turtle.left(90)
        turtle.fd(200)
        turtle.pendown()
        turtle.right(90)


        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(10,180)
        turtle.circle(25,110)
        turtle.left(50)
        turtle.circle(60,45)
        turtle.circle(20,170)
        turtle.right(24)
        turtle.fd(30)
        turtle.left(10)
        turtle.circle(30,110)
        turtle.fd(20)
        turtle.left(40)
        turtle.circle(90,70)
        turtle.circle(30,150)
        turtle.right(30)
        turtle.fd(15)
        turtle.circle(80,90)
        turtle.left(15)
        turtle.fd(45)
        turtle.right(165)
        turtle.fd(20)
        turtle.left(155)
        turtle.circle(150,80)
        turtle.left(50)
        turtle.circle(150,90)
        turtle.end_fill()
         
        turtle.left(150)
        turtle.circle(-90,70)
        turtle.left(20)
        turtle.circle(75,105)
        turtle.setheading(60)
        turtle.circle(80,98)
        turtle.circle(-90,40)


        turtle.left(180)
        turtle.circle(90,40)
        turtle.circle(-80,98)
        turtle.setheading(-83)


        turtle.fd(30)
        turtle.left(90)
        turtle.fd(25)
        turtle.left(45)
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(-80,90)
        turtle.right(90)
        turtle.circle(-80,90)
        turtle.end_fill()
         
        turtle.right(135)
        turtle.fd(60)
        turtle.left(180)
        turtle.fd(85)
        turtle.left(90)
        turtle.fd(80)
         

        turtle.right(90)
        turtle.right(45)
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(80,90)
        turtle.left(90)
        turtle.circle(80,90)
        turtle.end_fill()
         
        turtle.left(135)
        turtle.fd(60)
        turtle.left(180)
        turtle.fd(60)
        turtle.right(90)
        turtle.circle(200,60)
        turtle.up()
        turtle.goto(200,30)
        turtle.down()
        turtle.pencolor("red")
        turtle.write("宝宝，送你花花",font=("Arial",12,"normal"))

        
app = MyApp()
app.MainLoop()












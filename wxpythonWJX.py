import wx
import turtle
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent= None,
                         title='This is my tool!',
                         size = (400,200),
                         pos = (800,300))
        panel = wx.Panel(frame,-1)
        self.buttonWJX = wx.Button(panel,-1,'五角星',size=(75,75),pos=(150,10))
        self.Bind(wx.EVT_BUTTON,self.OnButtonWJX,self.buttonWJX)#按钮事件，绑定到下面的函数事件，绑定到上面生成的按钮
        frame.Show()
        return True
    def OnButtonWJX(self,event):#需要一个参数event才能将这个函数绑定到按钮上
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)
            
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()

'''import wx
app = wx.App()  #应用程序对象
frame = wx.Frame(parent = None)
frame.Show()
app.MainLoop()
'''
import wx

class MyFrame(wx.Frame):
    pass

class MyApp(wx.App):#继承wx
    def OnInit(self):
     frame = wx.Frame(parent = None)
     frame.Show()
     return True

if __name__== "__main__":
    app = MyApp()
    app.MainLoop()

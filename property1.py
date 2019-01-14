class Celsius:
    def __init__(self,value=26.0):
        self.value=float(value)

    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)

class Fahreheit:
    def __get__(self,instance,owner):
        return instance.cel*1.8+32        #当直接输入fah=10,x.fah怎么得到值的
    def __set__(self,instance,value):
        instance.cel=(float(value)-32)/1.8
class Temperature:
    cel=Celsius()
    fah=Fahreheit()
temp=Temperature()
print("初始状态：",temp.cel)
temp.cel=10
print("温度为10c时：",temp.fah)
temp.fah=87
print("fah为87时：{0:.1f}".format(temp.cel))

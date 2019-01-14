import math

class MingWen:
    def __init__(self,plaintext="abc"):
        self.plaintext=plaintext
    def __get__(self,instance,owner):
        return self.plaintext
    def __set__(self,instance,value):
        self.plaintext=value

class MiWen:
    def __get__(self,instance,owner):
        userinput=instance.mingwen
        
        list1=[]
        list2=[]
        #print("这是MiWen_userinput:",userinput)
        #print("这是长度：",len(userinput))
        def tras(userinput):
            dict1={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,
       "i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,
       "q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,
       "y":24,"z":25}
            #print("这是字典：",dict1["a"])
            print("这是tras_get_userinput: ",userinput)
            for i in userinput:
                list1.append(dict1[i])
        def JiaMiSuanFa():
                for i in range(0,len(userinput)):
                    list2.append(int(math.fmod(list1[i]*11+3,26)))
                #print("密文",list2)
        
        tras(userinput)
        JiaMiSuanFa()
        print("这是明文：%s,这是密文%s"%(list1,list2))
        instance.mingwen= list2
        return instance.mingwen
    def __set__(self,instance,value):
        list1=[]
        list2=[]
        
        def tras(value):
            dict1={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,
       "i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,
       "q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,
       "y":24,"z":25}
            #print("这是字典：",dict1["a"])
            #print("这是tras_set_userinput: ",value)
            for i in value:
                list1.append(dict1[i])
            #print("这是value_dict1:",list1)
        def JieMiSuanFa():
                #print("内部list1:",list1)
                for i in range(0,len(value)):
                    list2.append(int(math.fmod((list1[i]-3)*19,26)))
                #print("明文：",list2)
        tras(value)
        JieMiSuanFa()
        instance.mingwen=list2
        
class C:
    mingwen=MingWen()
    miwen=MiWen()

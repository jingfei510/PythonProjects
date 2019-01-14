import math
def tras():
    
    for i in userinput:
        list1.append(dict1[i])
def encryption():
    for i in range(0,len(userinput)):
        list2.append(int(math.fmod(list1[i]*11+3,26)))
        
dict1={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,
       "i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,
       "q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,
       "y":24,"z":25}

list1=[]
list2=[]
userinput="cryptographyandnetworksecurity"        
tras()
encryption()

try:
    f = open('try.py','r')
    l = f.read()
except:
    pass

with open('try.py','r') as f:
    z=f.read()
    print(z)

if 1:
    raise NameError('you erro')   #抛出异常

if 0:
     

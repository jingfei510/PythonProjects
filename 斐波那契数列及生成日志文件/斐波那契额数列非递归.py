a = 0
b = 1
c = a+b
number = int(input ("输出前几项的值："))
for i in range(1,number+1):
    print(c)
    c = a+b
    a,b=b,c
    


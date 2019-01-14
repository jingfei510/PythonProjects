def ferb(n):
    #递归
    if n<=1:
        return n
    else:
        return(ferb(n-2)+ferb(n-1))
number=int(input("输出前几项："))
if number <=0:
    print("请输入正整数")

else:
    for i in range(1,number+1):
        print(ferb(i))
#print(ferb(number-1))

import sys
##stdout_backup=sys.stdout
##log=open("ferb.log","w")   #生成日志文件

def ferb(n):
    #递归
    if n<=1:
        return n
    else:
        return(ferb(n-2)+ferb(n-1))
number=int(input("输出前几项："))
print(ferb(number-1))
##if number<=0:
##    print("请输入正整数")
##else:
##    #sys.stdout=log
##    for i in range(number):
##        print(ferb(i))    
##        #number=int(input("输出前几项："))
##if number<=0:
##    print("请输入正整数")
####else:
####    log.close()
####    sys.stdout=stdout_backup


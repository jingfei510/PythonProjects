def Fun(num):
	count=num//2
	while count>1:
		if num%count==0:
			print("%d最大公约数为%d"%(num,count))
			break
		count-=1
	else:
		print("%d是素数"%num)
num =int( input("enter number: "))
Fun(num)

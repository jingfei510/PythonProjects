class Fibs:
	def __init__(self,n=10):
		self.a=0
		self.b=1
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>self.n:
			raise StopIteration   #若引发异常，后面的代码不执行
		return self.a

f=Fibs(100)#实例化
for i in f:
    print(f)     #遍历

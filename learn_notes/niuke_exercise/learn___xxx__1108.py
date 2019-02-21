#learn __XXX__ 定制类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    #实现像一个list一样的[n]以及[n1:n2:step]
    def __getitem__(self,n):
    	self.a,self.b=1,1
    	#n为正整数
    	if isinstance(n,int):
   			#不支持负数，不能反向取值
    		for i in range(n):
    				self.a, self.b = self.b, self.a + self.b
    		return self.a
    	#n为切片
    	if isinstance(n,slice):
    		term_res=[]
    		res=[]
    		start=n.start
    		stop=n.stop
    		step=n.step
    		if start==None:
    			start=0
    		for i in range(start):
    			self.a, self.b = self.b, self.a + self.b
    		for i in range(start,stop):
    			term_res.append(self.a)
    			self.a, self.b = self.b, self.a + self.b
    		for i in range(len(term_res)//step):
    			res.append(term_res[i*step])
    		return res
f = Fib()
print(f[2:10:2])
#28.字符串”123″转换成123，不使用内置api，例如int（）
from functools import reduce
def f1(x):
    s={'1':1,'2':2,'3':3,'4':4,'5':5,'0':0}
    return s[x]
def f2(x,y):
    return x*10+y

r=reduce(f2,map(f1,'123'))
print(r)
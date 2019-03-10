'''
#9.请按alist中元素的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
res=sorted(alist,key=lambda x:x['age'],reverse=True)
print(res)
'''

'''
#10
a=[1,2,3]
a[10]:IndexError
a[5:]:  [],不会产生IndexError

'''

'''
11.写一个列表生成式，产生一个公差为11的等差数列
[x for x in range(1,100) if x%11==1]
[X*11 for X in range(10)]
'''

'''
12.给定两个列表，怎么找出他们相同的元素和不同的元素？
list1 = [1,2,3]
list2 = [3,4,5]
set:删除重复的元素
s1=set(list1)
s3=set(list2)
same=s1&s2 交集：相同的元素
different=s1^s2
all=s1|s2 并集：所有
r1=s1-s2 差集：在s1中不在s2中的元素
r2=s2-s1 差集：在s2中不在s1中的元素
'''


'''
13.请写出一段python代码实现删除list里面的重复元素？
set(list1)
'''

'''
16.python中内置的数据结构有几种？
a. 整型 int、 长整型 long、浮点型 float、 复数 complex
b. 字符串 str、 列表 list []、 元组 tuple ()
c. 字典 dict  {}、 集合 set,{},注意:set是无序不重复元素的集合
d. Python3 中没有 long，只有无限精度的 int
s1=set('aabbcc'):{'a','b','c'}
'''

'''
18.反转一个整数，例如-123 --> -321
def reverse(x):
    if -10<x<10:
        return x
    if x<=-10:
        s=str(x)
        s=s[1:]
        s=s[::-1]
        s=int(s)
        return -s
    if x>=10:
        return int(str(x)[::-1])
        
'''


'''
20.一行代码实现1-100之和
sum(range(1:101))
'''



'''
21.Python-遍历列表时删除元素
一、
赋值：相当于拷贝一份对象的引用，并不真的拷贝对象，所以赋值前后的id()一样，并没有开辟新的内存空间；
深拷贝/浅拷贝：都会重新创建内存空间，区别就在与子元素到底是否和原始列表共享。
浅拷贝：共享；深拷贝：不共享；
这些都属于浅拷贝：
1、完全切片操作[:]
2、list()，dict()
3、copy模块的copy()方法


二、
a = [1,2,3,4,5,6,7,8],删除小于5的数
a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))#[:]属于浅拷贝，所以两次id不同

删除列表多个元素的正确做法：
1.在新列表遍历，在旧列表删除
for i in a[:]:这儿a[:]相当于s=copy.copy(a)
    if i>5:
        pass
    else:
        a.remove(i)
    print(a)
print('-----------')
print(id(a))

2.内建函数filter
b=filter(lambda x:x>5,a)
print(b)

3.列表生成式：
b=[x for x in a if x>5]
print(b)

4.倒序删除
for i in range(len(a)-1,-1,-1):
    if a[1]>a:
        pass
    else:
        a.remove(a[i])
print(a)

三、
删除列表多个元素的错误做法：因为i在不断变大，但每删除一个元素list内元素就会向前移动
for i in a:
    if i>5:
        pass
    else:
        a.remove(i)
    print(a)

四、
删除List内单个元素：
1.list1.remove(val),无返回值
2.list1.pop(index),返回被删除的元素
    pop(),默认删除最后一个；append(),添加到末尾；
    这样，pop()+append() 类似于stack
3.del(list1[index]),无返回值

'''


'''
22.字符串的操作题目
def getMissingLetter(arg):
    low_arg=arg.lower()
    all=set('abcdefghijklmnopqrstuvwxyz')
    low_arg=set(low_arg)
    ret=''
    diff=all-low_arg#注意：两个set相减得到的还是一个set
    for i in diff:
        ret+=i
    print(ret)
    return ret
'''



'''
23.python 内置的数据类型：
可变类型：list ,dict,set
不可变类型：int,float,tuple,str
进行修改操作时，可变类型数据原地修改，直接修改内存中的值并没有开辟新的内存地址；
不可变类型的数据修改，并没有修改内存中的值而是开辟一块新的内存，将原值复制过来，
对这块新内存中的值进行操作。
'''

'''
24.is和==有什么区别？
is:比较两个对象的id值是否相等
==：比较两个对象的值是否相等
s1=[1],s2=[1]
s1==s2:True,s1 is s2:False
x1=1,x2=1
x1==x2:True
x1 is x2:True
'''



'''
26.用一行python代码写出1+2+3+10248
sum(1+2+3+10248)
reduce(lambda x,y:x+y,[1,2,3,10248])
'''


'''
27.Python中变量的作用域
函数作用域的LEGB顺序
1.什么是LEGB?
L： local 函数内部作用域
E: enclosing 函数内部与内嵌函数之间
G: global 全局作用域
B： build-in 内置作用
python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的

'''


'''
28.字符串”123″转换成123，不使用内置api，例如int（）
from functools import reduce
def f1(x):
    s={'1':1,'2':2,'3':3,'4':4,'5':5,'0':0}
    return s[x]
def f2(x,y):
    return x*10+y

r=reduce(f2,map(f1,'123'))
print(r)
'''
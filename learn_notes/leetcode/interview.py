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


'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
def find(arr,tar):
    d={}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            d[arr[i]+arr[j]]=[i,j]
    for k,v in d.items():
        if tar==k:
            return v
    return -1

print(find([2,7,11,15],9))
'''



'''
30.python代码实现删除一个list里面的重复元素
1.list(set(list1)) 注意：set返回的是一个set类型
2.将一个列表的数据取出放到另一个列表中，中间作判断
def set1(arr):
    res=[]
    for i in arr:
        if i not in res:
            res.append(i)
    return res
print(set1([1,2,3,2,3]))
3.使用字典
def set2(a):
    b = {}
    b = b.fromkeys(a)
    c = list(b.keys())
    print(c)
set2([1,2,3,2,3])
'''


'''
31.统计一个文本中单词频次最高的10个单词？
def count_word(filepath):
    word={}
    with open(filepath,"r",encoding="utf-8") as f:
        for line in f:
            lineone=line.split()
            for x in lineone:
                if not word.get(x):#第一次碰到x这个单词
                    word[x]=1
                else:
                    word[x]+=1
        firstTen=sorted(word.items(),key=lambda x:x[1],reverse=True)[:10]
        firstTen=[w[0] for w in firstTen ]
        print(firstTen)
'''


'''
32.请写出一个函数满足以下条件
该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
1、该元素是偶数
2、该元素在原list中是在偶数的位置(index是偶数)
arr=[0,1,2,3,4,5,6,7]
res=[x for x in arr[::2] if x%2==0]
或者：
res=[x for x in arr if x%2==0 and arr.index(x)%2==0]

'''


'''
34.用一行代码生成[1,4,9,16,25,36,49,64,81,100]
[x*x for x in range(1,11)]
'''


'''
35.输入某年某月某日，判断这一天是这一年的第几天？
from datetime import datetime
year=int(input())
month=int(input())
day=int(input())
day1=datetime.date(year=year,month=month,day=day)
day2=datetime.date(year=year,month=1,day=1)
days=(day1-day2).days+1
'''


'''
36.两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
def new_extend(l1,l2):
    res=[]
    i=0
    j=0
    while i<len(l1) and j <len(l2):
        if l1[i]<=l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    if i<len(l1):
        for x in l1[i:]:
            res.append(x)
    if j<len(l2):
        for y in l2[j:]:
            res.append(y)
    print(res)

new_extend([1,3,5],[2,4,6,7,8])
'''


'''
37.给定一个任意长度数组，实现一个函数
让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'135798642'
def fun(arg):
    res=''
    l1=[int(x) for x in arg if int(x)%2==1]
    l2=[int(y) for y in arg if int(y)%2==0]
    l1=sorted(l1)
    l2=sorted(l2,reverse=True)
    l1.extend(l2)
    for i in l1:
        res+=str(i)
    print(res)
    return res
fun('14656230282456664838')
'''


'''
三种排序：O(n^2)
def insertSort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        j=i-1
        while j>=0:
            if arr[j]>val:
                arr[j+1]=arr[j]
            else:
                break
            j-=1
        arr[j+1]=val
    print(arr)
    return arr
insertSort([8,7,6,5,4,3,2,1])


def bubbleSort(arr):
    for i in range(len(arr)):
        flag=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if flag==False:
            break
    print(arr)
    return arr

bubbleSort([8,7,6,4,2,1])

def selectSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)
    return arr

selectSort([8,7,6,4,2,1])



#归并排序
def mergeSort(arr):
    if len(arr)<=1:#如果没有这个判断，就会出现超过最大递归深度的报错。注意：递归一定要有终止条件
        return arr
    p=len(arr)//2
    left=mergeSort(arr[:p])
    right=mergeSort(arr[p:])
    return merge(left,right)


def merge(left,right):#left,right两个list
    tmp=[]
    i,j=0,0#注意：i,j=0,相当于只赋值给j
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1
    tmp.extend(left[i:])#可以写成：tmp+=left[i:]
    tmp.extend(right[j:])
    print(tmp)
    return tmp


mergeSort([3,2,1,4])



#快排
def quickSort(arr):
    if len(arr)<=1:
        return arr
    parti=partition(arr)
    return quickSort(arr[:parti])+quickSort(arr[parti:])


def partition(arr):#不断找出i的值，也就是放arr数组最后一个值的位置，要让前面的都小于pivot，后面的都大于pivot
    pivot=arr[-1]
    i=0
    for j in range(len(arr)-1):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[-1]=arr[-1],arr[i]#为什么这儿不能用pivot代替arr[-1]
    #注意：List里面存放的是元素的索引，也就是id
    return i



array = [4,2, 7, 6, 9, 5, 11, 3, 1, 8]
print(quickSort(array))


返回s2串在s1串中的位置
def find(s1,s2):
    if len(s2)>len(s1):
        return -1
    for i in range(len(s1)):
        if s1[i:i+len(s2)]==s2:
            return i
    return -1
print(find('www.taobao.com','taobao'))




2、	http的长连接和短连接是什么，各有什么优缺点，然后使用场景
HTTP协议:应用层协议，无状态面向连接，无状态可以理解为memoryless，即是两次HTTP请求之间没有记忆，
服务器不知道客户端是什么状态，无状态不代表HTTP不能保持TCP连接，
并不能说它的传输层就是udp，Http的传输层网络层用的是tcp/ip。


python里面的队列和栈：
1、栈：list相当于栈的功能
stack=[1,2,3,4]
stack.append(5)-入栈
stack.pop()-出栈
2、队列：
from collections import deque
queue=deque(['a','b','c','d'])
queue.append('e')-在队尾入队
queue.popleft()-在队头出队


'''
#尽量避免将可变对象作为函数的默认参数
def extendList(val, list=[]):
    print(id(list))
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList( 'a' )

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
m=[]
n=[]
print(id(m))
print(id(n))

def extendList1(val,list=None):
    #上面程序和下面程序结果不同，归根结底就是[]是可变对象，
    # 两个[]的地址id是不同的，但None是不可变对象，两个None的地址id是一样的
    if list==None:
        list=[]
    list.append(val)
    return list
q=None
p=None
print(id(q))
print(id(p))
'''
特殊方法计算一个整数N的二进制表示中有几个1
10001100 (n)

10001011 (n-1)

10001000 (n & (n-1))

可以看到底3位都变成了0。

如果你数学足够好，可以得出结论：

[结论]要消除整数n最低位的1，可以使用 n = n & (n-1)。
'''
def count_1(n):
    count=0
    while(n!=0):
        n=n&(n-1)
        count+=1
    print(count)
count_1(7)


'''
解法二：
整数n每次进行无符号右移一位，检查最右边的bit是否为1来进行统计，代码如下：
'''
def count_2(n):
    count=0
    while(n!=0):
        count+=n&1
        #这儿将n进行右移
        #n>>>1
    print(count)
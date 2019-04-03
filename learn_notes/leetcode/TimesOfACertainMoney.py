'''
回溯法凑出一个数
利用的是0-1背包的思想：
把所有物品放在一个list，每次对这个物品有两种处理方法：放进去或是不放
n=11,a1=1,a2=2,a3=1,a4=1,a5=2,a6=0
'''
r=[s.split('=') for s in input().split(',')]
n=int(r[0][1])
a=[int(i[1]) for i in r[1:]]
all={0:1,1:5,2:10,3:20,4:50,5:100}
A=[]
for i in range(len(a)):
    for j in range(a[i]):
        A.append(all[i])

times = 0

def f(i,n,a,m):
    global times
    if m==n:
        times+=1
        return 0
    if i==len(a):
        return 0
    f(i+1,n,a,m)#第i个物品不放进去
    f(i+1,n,a,m+a[i])#第i个物品放进在

f(0,11,A,0)
print(times)
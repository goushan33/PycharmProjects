#Process finished with exit code -1073741571 (0xC00000FD):pycharm栈溢出报错
#Segmentation fault (core dumped):linux栈溢出报错


import math
import sys
sys.setrecursionlimit(10000)
def cut(p,n):
    if n==0:
        return 0
    q=0
    for i in range(1,len(p)+1):
        q=max(q,p[i-1]+cut(p,n-i))
    print(q)
    return q
cut([1,5,8,9],4)


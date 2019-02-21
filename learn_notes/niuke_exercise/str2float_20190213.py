#str2float新函数--'123.456'-->123.456
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
#'.':'.'不能省略
def fn1(x,y):
    return x*10+y

def fn2(x,y):
    return x*0.1+y

def fn(s):
    return DIGITS[s]

def run(s):
    r=list(map(fn,s))
    index=r.index('.')
    r1=r[:index]
    r2=r[index+1:len(r)][::-1]
    sum1=reduce(fn1,r1)
    sum2=(reduce(fn2,r2))*0.1
    print(sum1+sum2)

run('123.456')




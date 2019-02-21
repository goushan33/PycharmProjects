import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, time.time()))
        return fn(*args,**kw)
    return wrapper

@metric
def Foo(a,b):
    return a+b

@metric
def add(a,b):
    return a+b+100

f=Foo(3,4)
print(f)
a=add(1,2)
print(a)
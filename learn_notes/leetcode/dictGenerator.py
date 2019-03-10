# 8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
def f(arg):
    res={}
    s=arg.split('|')
    for n in s:
        key,value=n.split(':')
        res[key]=int(value)
    print(res)
f("k:1 |k1:2|k2:3|k3:4")


#way2:字典生成式
arg="k:1 |k1:2|k2:3|k3:4"
res={key:int(value) for t in arg.split('|') for key,value in (t.split(':'),)}
print(res)



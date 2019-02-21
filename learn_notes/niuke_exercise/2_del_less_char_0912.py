
from collections import defaultdict
while True:
    try:
        a = input()
        dd = defaultdict(int)#用defaultdict，初始化的时候默认有个值，int则默认为0.这一点就和用Counter有类似的效果
        for i in a:
            dd[i] += 1

        for i in dd:
            print(i)
            if dd[i] == min(dd.values()):
                a = a.replace(i, "")
        print(a)
    except:
        break
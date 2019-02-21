
while True:
    try:
        num = int(input())
        x = []
        s=input()
        s1=s.split()
        for i in s1:
            x.append(int(i))

        res = []
        for k in range(num):
            term_num = 0
            x1 = x[0:k]
            x2 = x[(k + 1):num]
            for m in x1:
                if m >= x[k]:
                    term_num += 1
            for n in x2:
                if n >=x[k]:
                    term_num += 1
            res.append(term_num)
        res.sort()
        print(res[0])
    except:
        break
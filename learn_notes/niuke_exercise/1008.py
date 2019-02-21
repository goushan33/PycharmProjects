while True:
    try:
        stp = ''
        s = []
        r = []
        y=[]
        x=[]
        for line in iter(input, stp):
            s.append(line)
        n = int(s[0])
        m = int(s[1])
        s.pop(0)
        s.pop(0)
        for i in s:
            term = i.split()
            r.append(int(term[0]))
            y.append(int(term[1]))
            x.append((int(term[1]))/(int(term[0])))
        sum=0
        i=0
        res=0
        while sum<n and i<m:
            term1=max(x)
            t_index=x.index(term1)
            sum+=r[t_index]
            i+=1
            res+=y[t_index]
            r.remove(r[t_index])
            y.remove(y[t_index])
            x.remove(term1)
        print(res)
    except:
        break
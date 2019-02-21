while True:
    try:
        num=int(input())
        term1=input().split(',')
        index=int(term1[0])
        rem=int(term1[1])
        stp='end'
        s=[]
        for line in iter(input,stp):
            s.append(line)
        x=[]
        y=[]
        for i in s:
            x.append(int(i.split(',')[0]))
            y.append(int(i.split(',')[1]))
        for i in range(len(s)):
            if index <= num*(i+1) and index>=num*i:
                x[i] = x[i] + rem
                y[i] = y[i] - rem
                break
        for i in range(len(x)):
            print('%s,%s'%(x[i],y[i]))
    except:
        break

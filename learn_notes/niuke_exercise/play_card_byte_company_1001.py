while True:
    try:
        num=int(input())
        s=[]
        r=[]
        stp=''
        for line in iter(input,stp):
            s.append(line.split())
        for i in s:
          r.append([int(i[0]),int((i[1]))])
        for i in r:
            pass
    except:
        break

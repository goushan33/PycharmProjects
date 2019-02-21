while True:
    try:
        s=input()
        leng=len(s)
        i=0
        li=[]
        term_str = ''
        while i<leng:
            if 'A'<s[i]<'Z' or 'a'<s[i]<'z':
                term_str+=s[i]
            else:
                li.append(term_str)
                term_str = ''
                li.append(s[i])
            i=i+1
        if term_str!='':
            li.append(term_str)
        count=0
        for k in li:
            if k!=' ':
                pass



    except:
        break
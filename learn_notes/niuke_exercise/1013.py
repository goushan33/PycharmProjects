import re
from collections import defaultdict
while True:
    try:
        t_s = input()
        s = re.split(r'[^a-zA-Z]', t_s)
        term_s=s[::-1]
        dd=defaultdict(int)
        for i in s:
            if dd[i]==0:
                dd[i]+=1
        num=len(dd)-1

        res=''
        for key in dd:
            res+=key+' '
        print('The number of words in this passage is:%s,%s'%(num,res))
    except:
        break

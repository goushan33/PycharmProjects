import re
while True:
    try:
        s=input()
        s1=re.split(r'[^a-zA-Z]',s)
        r=s1[::-1]
        print(' '.join(r))
    except:
        break
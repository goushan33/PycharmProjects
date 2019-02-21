from itertools import combinations
while True:
    try:
        length = int(input())
        s = input().split()
        len1 = int(s[0])
        num1 = int(s[1])
        len2 = int(s[2])
        num2 = int(s[3])
        r1 = []
        r2 = []
        for i in range(num1):
            r1.append(len1)
        for i in range(num2):
            r2.append(len2)
        r = r1 + r2
        count=0
        for j in range(1,len(r)+1):
            res=list(combinations(r,j))
            for k in res:
                sum=0
                for m in k:
                    sum+=m
                if sum==length:
                    count+=1
        print(count)

    except:
        break
'''
给0-9 6个数字，组成最早或最晚的时间
不能组成时间就return false
'''
def generateTime():
    s=[]
    for i in range(6):
       s.append(int(input()))
    s.sort()
    if s[0]>=3:#小于等于2的数字必须要有一个
        return False
    count=0
    for i in s:
        if i<=5:
            count+=1
    if count<3:#小于等于5的数必须有三个
        return False
    if s[0]==2:
        if s[1]>=4:
            return False
        early='2'+str(s[1])+':'+str(s[2])+str(s[3])+':'+str(s[4])+str(s[5])
        print(early)
        maxn =s[1]
        for i in s[2:]:
            if i<4 and i>maxn:
                maxn=i
        late='2'+str(maxn)


print(generateTime())

'''
给0-9 6个数字，组成最早或最晚的时间
不能组成时间就return false
'''


def generateTime():
    s=[]
    for i in range(6):
       s.append(int(input()))
    s1=[]#小于等于2的
    s2=[]#等于3的
    s3=[]#小于等于5的,不包括s1和s2里面的
    for i in s:
        if i<=2:
            s1.append(i)
            s.remove(i)
    if len(s1)<1:
        return False
    for i in s:
        if i==3:
            s2.append(i)

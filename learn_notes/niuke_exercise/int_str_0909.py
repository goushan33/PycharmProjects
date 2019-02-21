#算法：整形int转字符串
def int_str(num):
    dict1={1:'1',2:'2',3:'3',4:'4'}
    t=[]
    r = []
    while num>0:
        s=num%10
        t.append(s)
        num//=10
    t=t[::-1]
    result=''
    for i in range(len(t)):
        result+=dict1[t[i]]
    print(result)
    print(isinstance(result,str))
int_str(41)


#字符串转整型：
def string_int(arg):
    dict1 = {'1':1,'2':2,'3':3,'4':4}
    t=[]
    sum=0
    for i in arg:
        t.append(dict1[i])
    for n in range(len(t)):
        sum=sum*10+t[n]
    print(sum)
    print((isinstance(sum,int)))
string_int('123')











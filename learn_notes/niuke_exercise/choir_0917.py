def find_longest_increasing_substring(s):
    num=len(s)
    longest=[1]*num#用longest list 记录以ai结束的最长递减子序列的长度，初始为1
    res=[[s[0]]]
    for j in range(1,num):#找到以Sj结尾的递减子序列
        term_res = []
        for i in range(0,j):
            if s[j]>s[i] and longest[j]<longest[i]+1:
                longest[j]+=1
                term_res.append(s[i])
        term_res.append(s[j])
        res.append(term_res)
    return longest


while True:
    try:
        num=int(input())
        x=[]
        s=input().split()
        for i in s:
            x.append(int(i))
        longest1=find_longest_increasing_substring(x)
        term_x=x[::-1]
        term_longest2=find_longest_increasing_substring(term_x)
        longest2=term_longest2[::-1]
        people_num_of_out=[]
        for i in range(num):
            people_num_of_out.append(num-(longest1[i]+longest2[i]-1))
        print(min(people_num_of_out))
    except:
        break
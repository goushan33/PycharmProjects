def find_longest_increasing_substring(s):
    num=len(s)
    longest=[1]*num#用longest list 记录以ai结束的最长递增子序列的长度，初始为1
    res=[[s[0]]]
    for j in range(1,num):#找到以Sj结尾的递增子序列
        term_res = []
        for i in range(0,j):
            if s[j]>s[i] and longest[j]<longest[i]+1:
                longest[j]+=1
                term_res.append(s[i])
        term_res.append(s[j])
        res.append(term_res)
    print(longest)
    print(res)
r=[10,22,9,33,21,50,41,60,80]
find_longest_increasing_substring(r)
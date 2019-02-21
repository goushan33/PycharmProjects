import sys
import re
while True:
    try:
        s=[]
        stp = ''
        for line in iter(input,stp):  #当没有接受到输入结束信号就一直遍历每一行
            s.append(line)
        print(s)
        for i in s:
            a = re.findall(r'(.{3,}).*\1', i)
            b1 = re.findall(r'\d', i)
            b2 = re.findall(r'[A-Z]', i)
            b3 = re.findall(r'[a-z]', i)
            b4 = re.findall(r'[^0-9A-Za-z]', i)

            if [b1, b2, b3, b4].count([]) <= 1 and len(i) > 8 and a == []:
                print('OK')
            else:
                print('NG')
    except:
        break
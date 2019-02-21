'''
import re
t = '21:05:30'
m= re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
'''


import re

line = "Cats are smarter than dogs"

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
searchObj=re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match!!")
#print(matchObj)
#print(searchObj)
text = "JGood is    a handsome boy, he is cool, clever, and so on..."
#用—替代字符串中的空格（至少一个），结果：JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
print(re.sub(r'\s+', '-', text))
#用lamdba进行复杂替换，将空格（一个）替换成[],结果：JGood[ ]is[ ][ ][ ][ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...
print(re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0))
#分割字符串，在空格（至少一个）位置分割，结果：['JGood', 'is', 'a', 'handsome', 'boy,', 'he', 'is', 'cool,', 'clever,', 'and', 'so', 'on...']
print(re.split(r'\s+', text,))
#获取字符串中所以匹配的字符串，如下是获取所有包含oo的子串，结果：['JGood', 'cool']
print(re.findall(r'\w*oo\w*', text))


'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
import re
test = 'bill323qqww.HGG@163.com'
#在[]内特殊字符，表示匹配特殊字符本身，不需要加反斜杠，[-./\]:匹配-或.或/或\
#在[]外特殊字符，表示匹配特殊字符本身，必须要加反斜杠
if re.match(r'^[a-zA-Z]+[0-9a-zA-Z.]+[0-9a-zA-Z]@(microsoft|gmail|163)\.com(\r\n|\n|\r)?$', test):
    print('ok')
else:
    print('failed')


'''
版本二可以提取出带名字的Email地址：
<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
'''
import re
def name_of_email(addr):
    m = re.match(r'((((\<[a-zA-Z\s]+\>)\s*([a-zA-Z]+)))|([a-zA-Z]+))@([a-zA-Z]+[0-9a-zA-Z.]+[0-9a-zA-Z])',addr)
    return m.group(1)

result=name_of_email('bgsggob@example.com')
print(result)



import re
def name_of_email(addr):
    m = re.match(r'((\<[a-zA-Z\s]+\>)?)\s*([a-zA-Z]+)@([a-zA-Z]+[0-9a-zA-Z.]+[0-9a-zA-Z])',addr)
    print(m)
    return m.group()




#r'((((\<[a-zA-Z\s]+\>)\s*([a-zA-Z]+)))|([a-zA-Z]+))@([a-zA-Z]+[0-9a-zA-Z.]+[0-9a-zA-Z])'
#r'((\<[a-zA-Z\s]+\>)?)((\s*)?)([a-zA-Z]+)@([a-zA-Z]+[0-9a-zA-Z.]+[0-9a-zA-Z])'
result=name_of_email('bob@example.com')
print(result)

text = "JGood is    a handsome boy, he is cool, clever, and so on..."
arg=re.split(r'\s+', text,)
print(len(arg))
print(arg[len(arg)-1])



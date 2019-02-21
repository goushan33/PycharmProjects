import re
s='021Abcd9Abcd'
a = re.findall(r'(.{3,}).*\1', s)
b1 = re.findall(r'\d', s)
b2 = re.findall(r'[A-Z]', s)
b3 = re.findall(r'[a-z]', s)
b4 = re.findall(r'[^0-9A-Za-z]', s)

print(a)
print(b1)
print(b2)
print(b3)
print(b4)

def encrypt(s1):
    r1=[]
    for i in s1:
        if i.isalpha():
            if i=='z':
                r1.append('A')
            if i=='Z':
                r1.append('a')
            if i>='a'and i<'z':
                r1.append(chr(ord(i)-32+1))
            if i>='A'and i<'Z':
                r1.append(chr(ord(i)+32+1))
        if i.isdigit():
            if i=='9':
                r1.append('0')
            else:
                r1.append(chr(ord(i)+1))
        if (not i.isdigit()) and ( not i.isalpha()):
            r1.append(i)
    print(''.join(r1))

def unencrypt(s2):
    r2=[]
    for i in s2:
        if i=='A':
            r2.append('z')
        if i=='a':
            r2.append('Z')
        if i>'A'and i<='Z':
            r2.append(chr(ord(i)-1+32))
        if i>'a' and i<='z':
            r2.append(chr(ord(i)-1-32))
        if i=='0':
            r2.append('9')
        if i>'0' and i<='9':
            r2.append(chr(ord(i)-1))
        if not i.isalpha()and not i.isdigit():
            r2.append(i)
    print(''.join(r2))

while True:
    try:
        s1=input()
        s2=input()
        encrypt(s1)
        unencrypt(s2)
    except:
        break
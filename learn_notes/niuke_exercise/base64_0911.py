import base64
def safe_base64_decode(s):
    if len(s)%4==0:
        r=base64.urlsafe_b64decode(s)
    else:
        for i in range(len(s)%4):
            s+=b'='
        r=base64.urlsafe_b64decode(s)
    return r
if b'abcd' == safe_base64_decode(b'YWJjZA'):
    print('测试成功')
else:
    print('测试失败')
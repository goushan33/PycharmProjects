#-*- coding: utf-8 -*-
import uuid

name = "test_name"
namespace_1 =uuid.uuid1()#这个namespace 可以是任意 uuid 字符串，你可以选择 uuid1 或者 uuid4 或者自己随便编造一个合法数据使用。这儿选取了python官方给的一个
namespace_2=uuid.NAMESPACE_DNS

print(uuid.uuid1())# 生成基于计算机主机ID和当前时间的UUID
print(uuid.uuid3(namespace_1, name))#基于命名空间和一个字符的MD5加密的UUID
print(uuid.uuid4())#随机生成一个uuid
print(uuid.uuid5(namespace_2, name))#基于命名空间和一个字符的SHA-1加密的UUID

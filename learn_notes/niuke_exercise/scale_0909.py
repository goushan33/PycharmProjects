#进制转换问题：


#转换为10进制
int('xxx',num)#把'xxx'的字符串当作num进制，然后转换为10进制，如果没有num,则默认'xxx'为10进制


#转换为16进制：
hex(12)				->	‘0xc’
#二进制：
hex(0b100)			->	‘0x4’
#八进制：
hex(0o11)			->	‘0x9’
hex(xxx)


#转换为8进制：

#十进制：
oct(12)				->	‘014’
#二进制：
oct(0b100)			->	‘04’
#十六进制：
oct(0x11)			->	‘021’


#转化为2进制

#十进制：
bin(12)			->	'0b1100'
#八进制：
bin(0o100)		->	'0b1000000'
#十六进制：
bin(0x11)		->	'0b10001'
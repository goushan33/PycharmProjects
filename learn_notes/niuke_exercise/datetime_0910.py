#注意：同一时刻，全球计算机的timestamp值是一样的

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime,timedelta,timezone
def to_timestamp(dt_str,tz_str):
    time_1=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    #用正则表达式提取出参数里的时区信息
    s1 = re.match(r'(UTC)((\+|\-)\d+):(.*)', tz_str)
    zone=int(s1.group(2))
    #计算题中的时区和本地时区差几个小时
    gap=8-zone
    #将参数时间换算成本地时间
    if gap>0:
        time_2=time_1+timedelta(hours=gap)
    else:
        time_2 = time_1-timedelta(hours=gap)
    return time_2.timestamp()
t1=to_timestamp('2015-5-31 16:10:30','UTC-09:00')
t2=to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
if t1==t2:
    print('测试通过')
else:
    print('测试失败')
    print(t1-t2)
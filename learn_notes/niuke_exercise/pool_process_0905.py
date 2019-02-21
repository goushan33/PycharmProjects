#part2
#random.random()随机生成一个[0，1）之间的实数
#time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数
from multiprocessing import Pool
import os,time,random

#子进程们许执行的任务
def subprocess(name):
    print('Subprocess(%s) %s start.'%(name,os.getpid()))
    start_time=time.time()
    time.sleep(random.random()*5)
    end_time=time.time()
    run_time=end_time-start_time
    print('Subprocess(%s) %s run for %0.2f seconds'%(name,os.getpid(),run_time))

#主进程
if __name__=='__main__':
    print('Father_process(%s) start'% os.getpid())
    p=Pool(3)#会产生‘等待’效果
    for i in range(5):
        p.apply_async(subprocess,args=(i,))#启动子进程
    print('running')
    p.close() #，调用join()之前必须先调用close()
    p.join()
    print('又回到主进程')
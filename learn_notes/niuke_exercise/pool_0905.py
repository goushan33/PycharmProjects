#0905
#windows中子进程的产生，Process

#part1
from multiprocessing import Process
import os
#子进程需要执行的任务
def child_process(s):
    print('child process(%s) %s' %(s,os.getpid()) )

#主进程
if __name__ == '__main__':
    print('Parent process start。')
    p1 = Process(target=child_process, args=('test',))#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    p1.start()
    p1.join()  # 等子进程执行结束再往下执行，通常用于进程间的同步
    print('又回到主进程 %s.' % os.getpid())
    p2 = Process(target=child_process, args=('test',))
    p2.start()
    p2.join()  # 等子进程执行结束再往下执行
    print('又回到主进程 %s.' % os.getpid())





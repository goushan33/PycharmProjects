#多线程，常用的两个模块，_thread(低级模块),threading（高级模块）,多用这个。
import time,threading

def new_thread():
    print('Thread %s is running'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('Thread %s is running>>>%s'%(threading.current_thread().name,n))
        time.sleep(2)
    print('END')

#注意这边没有【if __name__=='__main__'】语句，而是直接执行
'''
由于任何进程默认就会启动一个线程，
我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。
主线程实例的名字叫MainThread，
子线程的名字在创建时指定，
我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，
完全没有其他意义，
如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
print('Thread %s is running'%threading.current_thread().name)#获取当前线程名字：threading.current_thread().name
t=threading.Thread(target=new_thread,name='Loopthread')#创建Thread实例，注意不同于Process,第二个参数是name，而不是args
t.start()
t.join()
print('All is end.')




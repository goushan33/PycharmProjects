#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等.
#ThreagLocal 是一个局部变量，可以看作全局变量。是一个Class,获得了一个实例后可以添加局部变量进去
import threading

local_school=threading.local()#定义全局变量local_school
def thread_task():
    #获取当前线程关联的student信息
    std=local_school.student
    print('current thread is %s,current student is %s'%(threading.current_thread().name,std))

def run_thread(student_name):
    # 绑定ThreadLocal的student,可以将local_school看作一个class，可以在class里面添加变量
    local_school.student=student_name
    thread_task()

t1=threading.Thread(target=run_thread,args=('Student A',),name='Thread t1')
t2=threading.Thread(target=run_thread,args=('Student B',),name='Thread t2')
t1.start()
t2.start()
t1.join()
t2.join()




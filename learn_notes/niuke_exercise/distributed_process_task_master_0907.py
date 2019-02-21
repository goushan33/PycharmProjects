# encoding:utf-8
#分布式进程:
'''
首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
'''
'''
如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
现在，由于处理任务的进程任务繁重，
希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
原有的Queue可以继续使用，
但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了
'''

#首先完成服务进程,编写一个manager服务器，负责发送任务


# task_master.py

import random, time, queue
#managers是multiprocessing的子类
from multiprocessing.managers import BaseManager

# 发送任务的队列:（全局作用域）
task_queue = queue.Queue()
# 接收结果的队列:（全局作用域）
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
#正则表达式无法序列化，所以用这种标准函数
def get_task_queue():
    global task_queue
    return task_queue

def get_result_queue():
    global result_queue
    return result_queue

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
def test(host,port,authkey):
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)
    # 绑定端口, 设置验证码:
    manager = QueueManager(address=(host, port), authkey=authkey)
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=20)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
if __name__=='__main__':
    test('127.0.0.1',5000,b'abc')







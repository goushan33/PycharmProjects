#其次，完成任务模块
# task_worker.py
from multiprocessing.managers import BaseManager
import time,random,queue

class QueueManager(BaseManager):
    pass



def test(server_address,port,authkey):
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    m = QueueManager(address=(server_address, port), authkey=authkey)
    m.connect()
    task=m.get_task_queue()
    result=m.get_result_queue()
    print('Connect to server %s' % server_address)
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')

if __name__=='__main__':
    test('127.0.0.1',5000,b'abc')




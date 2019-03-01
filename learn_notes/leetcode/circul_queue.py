#基于数组实现循环队列
class CirculQueue(object):

    def __init__(self,capacity):
        self.items=[None]*capacity
        self.n=capacity
        self.head=0
        self.tail=0

    #入队
    def enqueue(self,val):
        #队列已满
        if (self.tail+1)%self.n==self.head:
            return False
        self.items[self.tail]=val
        self.tail=(self.tail+1)%self.n
        return True
    #出队
    def dequeue(self):
        #队列为空
        if self.tail==self.head:
            return  False
        ret=self.items[self.head]
        self.head=(self.head+1)%self.n
        return ret


q=CirculQueue(8)
q.enqueue(5)
q.enqueue(7)
print(q.dequeue())
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

def createlist(n):#包含n个节点的循环链表：
    head=Node(1)
    pre=head
    for i in range(2,n+1):
        newnode=Node(i)
        pre.next=newnode
        pre=newnode
    pre.next=head#尾节点指向头节点
    return head

def yuesefuhuan(n,m):
    head=createlist(n)
    cur=head
    pre=None
    while cur.next!=cur:
        for i in range(m-1):
            pre=cur#一定要把cur记录在pre里面，后面删除cur节点需要
            cur=cur.next
        print(cur.val)
        pre.next=cur.next
        cur.next=None
        cur=pre.next
    print(cur.val)


yuesefuhuan(8,2)


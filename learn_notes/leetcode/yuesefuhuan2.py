class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

def createlist(n):
    head=Node(1)
    cur=head
    for i in range(2,n+1):
        newnode=Node(i)
        cur.next=newnode
        cur=newnode
    cur.next=head
    return head

def yuesefuhuan(n,m):
    head=createlist(n)
    cur=head
    pre=None
    while cur.next!=cur:
        for i in range(m-1):
            pre=cur
            cur=cur.next
        print(cur.val)
        pre.next=cur.next
        cur.next=None
        cur=pre.next
    print(cur.val)


yuesefuhuan(8,2)

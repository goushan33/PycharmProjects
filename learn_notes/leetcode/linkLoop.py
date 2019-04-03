'''
首先，关于单链表中的环，一般涉及到一下问题：

1.给一个单链表，判断其中是否有环的存在；

2.如果存在环，找出环的入口点；

3.如果存在环，求出环上节点的个数；

4.如果存在环，求出链表的长度；

5.如果存在环，求出环上距离任意一个节点最远的点（对面节点）；

6.（扩展）如何判断两个无环链表是否相交；

7.（扩展）如果相交，求出第一个相交的节点
'''

class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
#1.给一个单链表，判断其中是否有环的存在；
def isLoopLink(head):
    slow=head
    fast=head
    while slow and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:#slow没向前进一步，fast进两步，表示slow和fast之间的距离缩短1
            print('loop')
            return True
    print('noloop')
    return False

#2.如果存在环，找出环的入口点；
def findEntranceofLoolLink(head):
    slow=head
    fast=head
    while slow and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:#slow没向前进一步，fast进两步，表示slow和fast之间的距离缩短1
            pr1 = head
            pr2 = slow
            while pr1 and pr2:
                pr1=pr1.next
                pr2=pr2.next
                if pr1==pr2:
                    return pr1
    print('noloop')
    return False

#3.如果存在环，求出环上节点的个数；
def countNumofLoopLink(head):
    slow=head
    fast=head
    while slow and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:#slow没向前进一步，fast进两步，表示slow和fast之间的距离缩短1
            count=1
            fast=fast.next
            while fast!=slow:
                count+=1
                fast=fast.next
            return count
    print('noloop')
    return False

#4.如果存在环，求出链表的长度；

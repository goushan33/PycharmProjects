#执行超时
import random
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def create_linkList(n):
	head = ListNode(1)
	pre = head
	for i in range(2, n+1):
		newNode = ListNode(random.randint(1,10))
		pre.next= newNode
		pre = newNode
	pre.next = head
	return head

class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        r = ListNode(0)
        res = r
        index = 0
        while (lists):
            i = 0
            mini = lists[0].val
            while i < k:
                if lists[i]:
                    if mini > lists[i].val:
                        mini = lists[i].val
                        index = i
                else:
                    del lists[i]
                    k -= 1
                i += 1
            r.next = lists[index]
            r = r.next
            lists[index] = lists[index].next
        return res.next

s=Solution()
l1=create_linkList(3)
l2=create_linkList(3)
l3=create_linkList(2)
lists=[l1,l2,l3]
res=s.mergeKLists(lists)
while(res):
    print(res.val)
    res=res.next


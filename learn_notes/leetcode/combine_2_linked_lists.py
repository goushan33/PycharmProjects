#合并 2个排序链表，返回合并后的排序链表1-2-4,1-2-3,变成1-1-2-3-4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode')-> 'ListNode':
        r = ListNode(0)
        res = r

        while (l1 and l2):
            if l2.val >= l1.val:
                r.next = l1
                r = r.next
                l1 = l1.next
            else:
                r.next = l2
                r = r.next
                l2 = l2.next
        if l1 == None:
            r.next = l2
        if l2 == None:
            r.next = l1
        return res.next


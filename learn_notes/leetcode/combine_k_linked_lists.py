# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        k = len(lists)
        if k == 0:
            return []
        if k == 1:
            return lists[0]
        val_list = []

        for i in lists:
            while (i):
                val_list.append(i)
                i = i.next
        val_list.sort(key=lambda x: x.val)
        r = ListNode(0)
        res = r
        for j in val_list:
            r.next = j
            r = r.next
        return res.next

'''
19. 删除链表的倒数第N个节点
执行用时: 48 ms, 在Remove Nth Node From End of List的Python3提交中击败了99.69% 的用户
内存消耗: 6.4 MB, 在Remove Nth Node From End of List的Python3提交中击败了95.75% 的用户

'''
#两次遍历的方法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int'):
        num = 0
        r = head
        s = head
        while (r != None):
            num += 1
            r = r.next
        if num == 1:  # 意思其实就是num=1,n=1
            return None

        if num == n:
            head = head.next
            return head

        if num > n:
            i = 1
            while (i < num - n):
                s = s.next
                i += 1
            term = s.next
            s.next = term.next
            return head





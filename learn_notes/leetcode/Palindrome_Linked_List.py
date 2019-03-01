# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#快慢指针找到中点
#将后半部分指针反向
#基表前后两半的值
class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':

        if head == None or head.next == None:
            return True

        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        pre = None
        slow = slow.next
        while (slow):#链表反转
            r = slow.next
            slow.next = pre
            pre = slow
            slow = r

        while pre != None and head != None:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True




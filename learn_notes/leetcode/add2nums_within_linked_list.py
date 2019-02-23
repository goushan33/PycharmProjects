# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        l1,l2:ListNode
        '''
        carry = 0  # 进位
        res = ListNode(0)  # 先随便初始化res,反正最后结果返回的是res.next
        r = res  # 将r指向res,然后在程序里操作r,这样res就还是指向头节点。这一点很聪明
        while (l1 or l2):
            # 注意这儿为什么不是l1.next or l2.next,假如l1和l2都是一个节点，这样不是循环根本无法进行下去吗
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10  # 计算进位
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next

        if (carry != 0):
            r.next = ListNode(carry)
        return res.next




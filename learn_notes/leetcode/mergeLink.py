'''
合并两个有序链表
'''
def mergeLink(link1,lin2):
    res=None
    while link1 and lin2:
        if link1.val<=lin2.val:
            res.next=link1
            res = res.next
            link1=link1.next
        else:
            res.next=link2
            res=res.next
            link2 = link2.next
    if link1:
        res.next=link1
    else:
        res.next=link2
    return res

'''
按层打印一棵树

理解好队列，可以很容易的解决树的层此遍历，步骤如下：

       1.首先将根节点放入队列中。
       2.当队列为非空时，循环执行步骤3到步骤5，否则执行6；
       3.出队列取得一个结点，访问该结点；
       4.若该结点的左子树为非空，则将该结点的左子树入队列；
       5.若该结点的右子树为非空，则将该结点的右子树入队列；
       6.结束。
'''

import queue
import random

#定义树的节点
class TreeNode:
    def __init__(self, val,left=None,right=None):#写成这样方便创建二叉树
        self.val = val
        self.left= left
        self.right=right

     # 这一步是在每次调用某个结点时，自动调用.data的方法
    def __str__(self):
        return str(self.val)


#创建一个满二叉树：
def createTree():#包含n个节点

    A = TreeNode('A', 'B', 'C')
    B = TreeNode('B', None, 'D')
    C = TreeNode('C', 'E', 'F')
    E = TreeNode('E', 'G', None)
    F = TreeNode('F', 'H', 'I')
    return A
'''
A=createTree()
print(A.val,A.left)
q=queue.Queue(maxsize=0)
q.put(A)
cur=q.get()
print(cur.val)
'''
def printTree(root):
    if not root:
        return None
    res=[]
    q=queue.Queue(maxsize=0)
    q.put(root)
    while not q.empty():
        cur=q.get()
        print(cur.val)
        if cur.left!=None:
            q.put(root.left)
        if cur.right!=None:
            q.put(root.right)
        res.append(cur.val)
    print(res)
    return res

A=createTree()
printTree(A)
'''

前序遍历：先访问根节点，再访问左子树，最后访问右子树

中序遍历：先访问左子树，再访问根节点，最后访问右子树

后序遍历：先访问左子树，再访问右子树，最后访问根节点

层序遍历：每一层从左到右访问每一个节点。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归方法：不能把所有程序写在一个函数里面，不然每次子调用会新建一个局部变量res，每次的res都空了
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if root == None:
            return
        res.append(root.val)
        if root.left != None:
            self.preorder(root.left, res)
        if root.right != None:
            self.preorder(root.right, res)


'''非递归方法;
1.首先把根节点压入栈中
2.此时栈顶元素即为当前根节点，弹出并访问即可
3.把当前根节点的右子树和左子树分别入栈，考虑到栈是先进后出，所以必须右子树先入栈，左子树后入栈
4.重复2,3步骤，直到栈为空为止
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        if root == None:
            return res
        stack.append(root)
        while (stack != []):
            r = stack.pop()  # 记住：pop是有返回值的，返回被删除的元素
            res.append(r.val)
            if r.right != None:
                stack.append(r.right)
            if r.left != None:
                stack.append(r.left)
        return res


#中序遍历：左节点-根节点-右节点
#递归方法：
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if root == None:
            return
        self.inorder(root.left, res)#不要细想递归运行的流程，只需要找到分解公式
        res.append(root.val)
        self.inorder(root.right, res)

#非递归方法：
#需要额外的一个指针nodep来记录下次待访问的节点

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res
        stack = []
        nodep = root
        # 用nodep这个指针来记录下次待访问的节点
        while stack != [] or nodep != None:
            if nodep != None:
                stack.append(nodep)
                nodep = nodep.left
            else:
                r = stack.pop()
                res.append(r.val)
                nodep = r
                if nodep.right != None:
                    stack.append(nodep.right)
                    nodep = nodep.right.left  # p始终为下一个待访问的节点
                else:
                    nodep = None
        return res

#后序遍历：左节点-右节点-根节点
#递归方法：
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if root == None:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

#非递归方法：
'''
另一种解法，大家可以看看前序遍历的非递归版本，
访问顺序依次是根节点->左子树->右子树，如果将压栈顺序改动一下，
可以很容易得到根节点->右子树->左子树，
观察这个顺序和后序遍历左子树->右子树->根节点正好反序。
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if root==None:
            return res
        stack=[]
        stack.append(root)
        while stack!=[] :
            r = stack.pop()  # 记住：pop是有返回值的，返回被删除的元素
            res.append(r.val)
            if r.left != None:
                stack.append(r.left)
            if r.right != None:
                stack.append(r.right)
        return res[::-1]


#层序遍历，这样出来的结果是不分层的：【a,b,c,d,e,f,g】这样
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root==None:
            return res
        queue=deque([])
        queue.append(root)
        while queue!=deque([]):
            r=queue.popleft()
            res.append(r.val)
            if r.left!=None:
                queue.append(r.left)
            if r.right!=None:
                queue.append(r.right)
        return res

#层序遍历：分称王打印结果：输出示例：[[3],[9,20],[15,7]]
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root==None:
            return res
        q=deque([])
        q.append(root)
        tmp=[]
        tmp_q=deque([])
        while q!=deque([]):
            r=q.popleft()
            tmp.append(r.val)
            if r.left!=None:
                tmp_q.append(r.left)
            if r.right!=None:
                tmp_q.append(r.right)
            if q==deque([]):
                q=tmp_q
                tmp_q=deque([])
                res.append(tmp)
                tmp=[]
        return res
题目：
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?


1.Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.result = self.traverse(root)
        return self.result
    def traverse(self, root):
        
        if not root:
            return
###顺序是左右根
        self.traverse(root.left)
        self.traverse(root.right)
        self.result.append(root.val)
        return self.result
        
        
2.Non-recursive
终于找到一个简单易懂的Non-recursive方法
利用两个栈，在s1中按照根左右的顺序push进node，然后将右node pop出，再循环；即相当于将整个结果反着push进s2，这样s2 pop时的顺序就是postorder的顺序
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        s1 = [root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            
        while s2:
            result.append(s2.pop().val)
        return result

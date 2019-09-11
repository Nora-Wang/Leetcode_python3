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


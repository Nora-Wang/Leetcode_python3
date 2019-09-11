题目：
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?



1. Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        self.result = []
        self.result = self.traverse(root)
        return self.result
    def traverse(self, root):
        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)
        return self.result
        
2. Non-recursive

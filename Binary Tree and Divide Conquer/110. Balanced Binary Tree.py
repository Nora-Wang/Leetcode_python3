题目：
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.


推荐用version1，因为定义了IsBalanced，代码清晰，更好理解
version2用-1做标记，容易出错


1. Version九章
divide and conquer
用两个值分别代表深度和平衡性
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, isbalanced = self.maxdepth(root)
        
        return isbalanced
    
    def maxdepth(self, root):
        if not root:
            return 0, True
        
        left_depth, left_isbalanced = self.maxdepth(root.left)
        if not left_isbalanced:
            return 0, False
        
        right_depth, right_isbalanced = self.maxdepth(root.right)
        if not right_isbalanced:
            return 0, False
        
        return max(left_depth, right_depth) + 1, abs(left_depth - right_depth) <= 1
        

        
        
        
2.Simple Version
思想：divide and conquer
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    #利用dfs函数的返回值作为标志，若为-1则说明不平衡，反之则平衡
    def dfs(self, root):
        if not root:
            return 0
            
        #divide
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        #conquer
        #左子树或右子树不平衡时
        if left == -1 or right == -1:
            return -1
        
        #左右子树高度差>1时
        if abs(left - right) > 1:
            return -1
            
        #返回该root的高度，以便于后续node的高度计算（即下一层直接+1）
        return max(left, right) + 1
    
    def isBalanced(self, root):
        if self.dfs(root) == -1:
             return False
        return True
        
        

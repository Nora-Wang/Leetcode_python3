题目：
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6


code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left_max = self.helper(root.left)
        right_max = self.helper(root.right)
        
        
        self.res = max(self.res, left_max + right_max + root.val)
        
        curt = max(left_max, right_max) + root.val
        
        return curt if curt > 0 else 0

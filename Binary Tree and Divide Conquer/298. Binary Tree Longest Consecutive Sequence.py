Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

#05/10/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
divide and conquer
every level recursion left and right
1. rules
use gloable variable to record LCS, use divide and conquer to get curt LCS, return to the upper level
2. return
for curt root, if root.left/right exist and root.val == root.left/right.val - 1, return left/right + 1; else 1
3. edge case
not root, return 0

time: O(n), space:O(1)
'''
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.lcs = 1
        self.helper(root)
        
        return self.lcs
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if root.left and root.left.val - 1 == root.val:
            self.lcs = max(self.lcs, left + 1)
            return left + 1
        
        if root.right and root.right.val - 1 == root.val:
            self.lcs = max(self.lcs, right + 1)
            return right + 1
        
        return 1
        
            



用一个temp来记录path

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        
        self.helper(root, [])
        
        return self.res
        
    def helper(self, root, temp):
        if not root:
            return
        
        if temp and temp[-1] + 1 == root.val:
            temp.append(root.val)
        else:
            temp = [root.val]
        
        self.res = max(self.res, len(temp))
        
        self.helper(root.left, temp)
        self.helper(root.right, temp)
        
        #backtracking
        temp.pop()
        

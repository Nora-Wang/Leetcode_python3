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
        
        
        temp.pop()
        

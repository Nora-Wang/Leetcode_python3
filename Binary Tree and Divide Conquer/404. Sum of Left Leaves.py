Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
need get all left leaves sum -> saperate to left and right subtree -> use divide and conquer
1. rule
get left sum and right sum
2. end case
if not root -> return 0
curt root.left is a leaf -> return left + right + root.left.val

time: O(N), space: O(1)

'''

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        
        if root.left and not root.left.left and not root.left.right:
            return left + right + root.left.val
        return left + right

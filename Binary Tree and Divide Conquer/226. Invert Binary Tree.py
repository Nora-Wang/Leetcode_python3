Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

# 2026/01/16
# Recursion - top to down
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root
    
    def helper(self, root):
        if not root:
            return
        
        if not root.left and not root.right:
            return
        
        root.left, root.right = root.right, root.left
        self.helper(root.left)
        self.helper(root.right)
        return
        
# Divide and Concur - down to top
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left

        return root




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
root: the same

1. base case: root == None, return None
2. recursion rule: use divide and conquer to get left and right -> left and right have been inverted
(just think about the second level), make root.left = right, root.right = left
3. return value: inverted result for curt root
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left, root.right = right, left
        
        return root
        

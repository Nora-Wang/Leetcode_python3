Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4


code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
uni-value subtree: left/None = root = right/None -> use recursion to count how many nodes in the subtree they match the rules

1. definition
helper(root)
2. rules
for curt root, left/right subtree are uni-value + compare root/left/right val, there has a situation: left/right is None
3. return 
True/False -> curt root is Uni-value
4. edge case
not root, return True

time O(n), space O(1)

'''

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        self.helper(root)
        
        return self.count
    
    def helper(self, root):
        if not root:
            return True
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left and right and (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val):
            self.count += 1
            return True
        
        return False

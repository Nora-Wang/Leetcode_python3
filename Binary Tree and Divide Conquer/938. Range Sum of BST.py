Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.


code:
#直接递归解法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        result = 0
        
        if L <= root.val <= R:
            result += root.val
        
        if root.left:
            result += self.rangeSumBST(root.left, L, R)
        if root.right:
            result += self.rangeSumBST(root.right, L, R)
        
        return result
        
        
        
#使用preorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.preorder(root, L, R)
    
    def preorder(self, root, L, R):
        if not root:
            return 0
        
        left = self.preorder(root.left, L, R)
        right = self.preorder(root.right, L, R)
        
        if L <= root.val <= R:
            return left + root.val + right
        
        return left + right

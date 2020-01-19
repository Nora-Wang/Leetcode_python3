Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

Example

Example1

Input: root = {2,1,3}, p = 1
Output: null
Example2

Input: root = {2,1}, p = 2
Output: 1
Notice

If the given node has no in-order predecessor in the tree, return null


直接参考285即可

code:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        self.result = None
        self.prev = None
        self.helper(root, p)
        
        return self.result
    
    def helper(self, root, p):
        if not root or self.result:
            return
        
        self.helper(root.left, p)
        if root == p:
            self.result = self.prev
            
        self.prev = root
        
        self.helper(root.right, p)

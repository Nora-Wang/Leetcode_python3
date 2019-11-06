Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
          
          
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if not root:
            return root
            
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        return right_last or left_last or root
        
            
            
        
            
        

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


divide and conquer,将左右子树调换即可

code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        #注意这里的写法，python用,时，两个步骤可以同时进行，这样可省去使用record
        root.left, root.right = right, left
        
        return root
        

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
   
code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(preorder, inorder)
        
    def build_tree(self, preorder, inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        root_index = inorder.index(preorder[0])
        
        root.left = self.build_tree(preorder[1:root_index + 1], inorder[:root_index])
        #这里的inorder直接跳过了该根
        root.right = self.build_tree(preorder[root_index + 1:], inorder[root_index + 1:])
        
        return root
        
        
        

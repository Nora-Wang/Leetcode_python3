Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
   
参考105

code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(inorder, postorder)
    
    def build_tree(self, inorder, postorder):
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        
        root_index = inorder.index(postorder[-1])
        
        root.left = self.build_tree(inorder[:root_index], postorder[:root_index])
        root.right = self.build_tree(inorder[root_index + 1:], postorder[root_index:-1])
        
        return root

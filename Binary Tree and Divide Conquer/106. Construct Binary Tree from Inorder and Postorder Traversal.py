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
Base case: if preorder is a empty list, it means there is no root, so return None

Recursion rule:
1. preorder: last node is curt root.val, curt_root_value
2. inorder: index = inorder.index(curt_root_value), [:index] -> root.left, [index + 1:] -> root.right
3. preorder: utilize index in the inorder, which means the length of left/right part
   [:index] -> root.left, [index:-1] -> root.right
    
Return value: the curt created root

time: O(n^2), n = num of nodes in the tree
space: O(n)

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
        
        # 跟105一样，如果想要减少时间复杂度，则可以用hashtable = {value:index}来预处理inorder，这样就能在O(1)的时间内找到postorder[-1]对应的index
        # 这样最终time: O(n)
        root_index = inorder.index(postorder[-1])
        
        root.left = self.build_tree(inorder[:root_index], postorder[:root_index])
        root.right = self.build_tree(inorder[root_index + 1:], postorder[root_index:-1])
        
        return root

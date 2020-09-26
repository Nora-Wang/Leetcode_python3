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
   
'''
utilize the preorder and inorder rules

Base case: if preorder is a empty list, it means there is no root, so return None

Recursion rule:
1. preorder: first node is curt root.val, curt_root_value
2. inorder: index = inorder.index(curt_root_value), [:index] -> root.left, [index + 1:] -> root.right
3. preorder: utilize index in the inorder, which means the length of left/right part
   [1:1+index] -> root.left, [1+index:] -> root.right
    
Return value: the curt created root

time: O(n^2), n = num of nodes in the tree
space: O(1)
'''
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
        
        
        
# 上面的方法由于inorder.index(preorder[0])，导致每次recursion的时候都是O(n) -> 最后的时间复杂度为O(n^2)
# 可以对inorder进行预处理，使用hashtable = {value:index}来记录，这样在利用preorder[0]找到inorder对应的index的时候，时间为O(1) -> 最后的时间复杂度为O(n)
# time: O(n), space: O(n)(hashtable)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # {value:index}
        hash_inorder = {}
        for index, value in enumerate(inorder):
            hash_inorder[value] = index
            
        return self.helper(preorder, inorder, hash_inorder)
        
    def helper(self, preorder, inorder, hash_inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        index = hash_inorder[preorder[0]]
        
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return root

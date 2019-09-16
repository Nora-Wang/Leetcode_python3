题目：
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true


思路：
Version1：
仔细看题目，只存在比root大和比root小的情况，不存在等于的情况，因此可以直接利用BST的性质：若inorder traversal的结果是升序的，则为BST
注意这里inorder的时候若用traversal，需要与前一个node.val比较，若发现更小，则不是升序

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inorder(root)
            
        
    def inorder(self, root):
        
        if not root:
            return True
        
        stark = []
        res = []
        
        while root or stark:
            while(root):
                stark.append(root)
                root = root.left
            root = stark.pop()
            if res == [] or root.val > res[-1]:
                res.append(root.val)
                root = root.right
            else:
                return False
            
        return True
        
若inorder用divide and conquer，则需要记录left.max和right.min，以此与root.val做比较


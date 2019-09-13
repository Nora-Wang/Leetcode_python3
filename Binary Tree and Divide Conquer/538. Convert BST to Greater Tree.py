题目：
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13



思路：
用sum记录右侧数据，将sum += 根，此时sum=根+右的值；运算到左时，将sum += 左，即sum = 右+根+左


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        root.right = self.convertBST(root.right)
        
        self.sum += root.val
        root.val = self.sum
        
        root.left = self.convertBST(root.left)
        
        return root

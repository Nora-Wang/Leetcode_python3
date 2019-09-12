题目：
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3




1.Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        #不能return None，因为整个结果是一个list，应该返回一个空list
        if not root:
            return []
    
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        
        #由于输出结果，需要注意写法，都是str
        #这里的思想是当以root点为根的leftPath已经完成，当将整个path加入result中时，要从root开始，一个node一个node的顺下去
        for node in leftPath:
            result.append(str(root.val) + '->' + str(node))
        for node in rightPath:
            result.append(str(root.val) + '->' + str(node))
            
        #这道题做完后再将单node的情况带入，会发现多了‘->’，因此需要单独写append的格式
        if root.left == None and root.right == None:
            result.append(str(root.val))
            
        return result

                

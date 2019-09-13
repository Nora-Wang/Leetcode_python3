题目：
给定一个二叉树，从根节点root出发，求最大路径和，可以在任一点结束

思路：
1.如果是求从root到leaf的最大路径，就用分治法，从上到下，每个节点的最大路径是其左子树和右子树的最大路径的最大值:
  root.val + max(left, right)
2.如果二叉树上的节点值有负数，那么最大路径就有可能不到leaf就结束了，所以在计算节点最大路径时，如果其左右子树最大路径的最大值为负数，
  则该节点到leaf的最大路径长度应该为0：root.val + max(0, left, right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left = self.maxPathSum(root.left)
        right = self.maxPathSum(root.right)
        
        max_sum = root.val + max(0, left, right)
        
        return max_sum
        
        

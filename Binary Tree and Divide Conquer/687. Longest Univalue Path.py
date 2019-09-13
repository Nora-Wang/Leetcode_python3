题目：
Given a binary tree, find the length of the longest path where each node in the path has the same value. 

This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \  
          4   4  
Output: 2     

思路：

判断当root.val == root.left.val时，此时从root左侧的longest path就是 root.left的最长路径+1；
   当root.val == root.right.val时，此时从root右侧的longest path就是 root.right的最长路径+1
   最后的longest path应为左侧+右侧
   


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.arrow_length(root)
        return self.count
    
    def arrow_length(self, root):
        
        if not root:
            return 0
        
        left_count = self.arrow_length(root.left)
        right_count = self.arrow_length(root.right)
        
        #这里需要另设arrow而不用count，是因为（参考上面的example）当node = 4得出其最大路径为1，但4 != root 5，因此5的左侧最大路径需要清0,
        #即直接等于left_arrow = 0
        left_arrow = right_arrow = 0
        
        if root.left and root.val == root.left.val:
            left_arrow = left_count + 1
        
        if root.right and root.val == root.right.val:
            right_arrow = right_count + 1
            
        #这里需要与self.count自己比较大小是因为，当运行到最后，即root时(如example),其左+右=1，但之前在node4的时候得出的值为2，因此应该返回2
        #即其只返回left_arrow + right_arrow，得到的值只是root的length of the longest path
        #但若出现不以root为根的node的length of the longest path更大，则无法返回
        #因此需要比较，若root的结果更大则返回其值；反之，则返回之前node所得值
        self.count = max(self.count, left_arrow + right_arrow)
        
        return max(left_arrow, right_arrow)
    
        

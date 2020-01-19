Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          [] 
          
          

code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.leaves = []
        
        self.helper(root)
        
        return self.leaves
    
    def helper(self, root):
        #叶子下面的点的值设置为-1，则叶子点为0 
        if not root:
            return -1
        
        #左右分治
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)
        
        #记录当前高度
        root_height = max(left_height, right_height) + 1
        
        #如果当前高度太高，再结果中新开一个list[]
        if root_height == len(self.leaves):
            self.leaves.append([])
        
        #对应层高加入当前结点的值
        self.leaves[root_height].append(root.val)
        
        #返回当前高度,以便后续node高度的计算
        return root_height
    

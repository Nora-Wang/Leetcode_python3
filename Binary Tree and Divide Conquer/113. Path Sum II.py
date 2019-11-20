Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]



code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(root, [], sum, results)
        
        return results
    
    def dfs(self, root, path, target, results):
        if not root:
            return
        
        path.append(root.val)
        
        if target == root.val and not root.left and not root.right:
            return results.append(list(path))
        
        self.dfs(root.left, list(path), target - root.val, results)
        self.dfs(root.right, list(path), target - root.val, results)
        

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.



#recursion (DFS)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        self.res = False
        self.dfs(root, sum, root.val)
        
        return self.res
        
    def dfs(self, root, sum, temp):
        if not root.left and not root.right:
            if temp == sum:
                self.res = True
            return
        
        if root.left:
            self.dfs(root.left, sum, temp + root.left.val)
        if root.right:
            self.dfs(root.right, sum, temp + root.right.val)

#4/6/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, sum, 0)
    
    def helper(self, root, sum, curt):
        if not root:
            return False
        
        if not root.left and not root.right:
            return curt + root.val == sum
        
        return self.helper(root.left, sum, curt + root.val) or self.helper(root.right, sum, curt + root.val)



用recursion分析不同情况

code:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
            
        #叶节点时
        elif root.val == sum and not root.left and not root.right:
            return True
        #recursion左子树和右子树
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
        

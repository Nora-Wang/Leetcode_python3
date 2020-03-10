题目：

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


#Version 0
#recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
    
    
#Version 1
#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        
        depth = 0
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth









思路：
利用divide conquer(dfs)思想，叶节点的下一层为0，往上依次加一，找出左右最大的depth




code:
leetcode version
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
          #此处返回值为0，因为叶节点的下一层的depth为0，叶节点为1
            return 0
        #因为调用自身函数，因此需要用self.
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        result = max(leftDepth, rightDepth) + 1
        
        return result

    
lintcode version
1. divide and conquer
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0
            
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

2.traversal
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.depth = 0
        
    def maxDepth(self, root):
        self.traverse(root, 1)
        return self.depth
        
    def traverse(self, root, cur_depth):
        if not root:
            return
        
        self.depth = max(self.depth, cur_depth)
        self.traverse(root.left, cur_depth + 1)
        self.traverse(root.right, cur_depth + 1)
        

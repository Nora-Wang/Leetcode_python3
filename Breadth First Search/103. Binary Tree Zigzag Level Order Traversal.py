题目：
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


思路：
BFS模板，version1使用变量count记录level，偶数时用reverse翻转；version2使用变量rev记录level，为True时翻转

code:

Version 1:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        count = 1
        while queue:
            level = []
            len_level = len(queue)
            i = 0
            while i < len_level:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            if count % 2 == 0:
                level.reverse()
            result.append(level)
            count += 1
        return result
        
Version 2:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        rev = False
        while queue:
            level = []
            len_level = len(queue)
            i = 0
            while i < len_level:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            if rev:
                level.reverse()
            result.append(level)
            rev = not rev
        return result
        

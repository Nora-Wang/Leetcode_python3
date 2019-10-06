题目：
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

思路：
同107，最后result.reverse()一下就行
需要注意的是不能这样写：return result.reverse()，因为result.reverse()是一个使result翻转的函数调用，其本身是不返回值的，这样的结果是[]

注意循环使用for _ in range(len_level):

code: 
    
Version 0
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            result.append([item.val for item in queue])
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        result.reverse()
        return result
    
    
Version 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            result.append([item.val for item in queue])
            len_level = len(queue)
            i = 0
            while i < len_level:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        result.reverse()
        return result

题目：
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]


思路：
直接就用BFS的模版,利用二叉树的特性（只有左右两个子树）
主要需要设置：
result(记录最后的结果)
queue(利用队列FIFO的定义，先将第一层的node全部放入queue里，再将它们的left和right节点，即第二层的节点全部放入queue，这样pop的时候就是按层级pop的)
level(参考结果，需要讲每层的node分隔)


version 0和version 1速度的快慢主要是循环的写法造成的，需使用for _ in range(len_level)


code:
Version 0: 94%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level = []
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                ###注意是node.val!!
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level = []
            i = 0
#这里需要用len_level记录一下queue的长度，因为在循环里queue的长度是变化的
            len_level = len(queue)
            while i < len_level:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            result.append(level)
        return result
        
Version 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            i = 0
#在queue循环的时候就直接将当前node全部加入到result里(注意这里是append.([]))，这样就不用设置level，后续可直接将左右节点加到queue里
            result.append([item.val for item in queue])
            len_level = len(queue)
            while i < len_level:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        return result
            
            

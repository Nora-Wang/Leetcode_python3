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

# 01/06/2026
# BFS
# Time O(n), Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque([root])

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(list(temp))
        
        return res
                
# DFS
# Use a hashmap to record the nodes in every level with depth {depth : [list of node value]}
# Time O(logn ~ n), Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.record = collections.defaultdict(list) # {depth : [list of node value]}

        self.dfs(root, 0)

        return [value for key, value in sorted(self.record.items(), key = lambda item:item[0])]
    
    def dfs(self, root, depth):
        if not root:
            return
        
        self.record[depth].append(root.val)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)



思路：
直接就用BFS的模版,利用二叉树的特性（只有左右两个子树）
主要需要设置：
result(记录最后的结果)
queue(利用队列FIFO的定义，先将第一层的node全部放入queue里，再将它们的left和right节点，即第二层的节点全部放入queue，这样pop的时候就是按层级pop的)
level(参考结果，需要讲每层的node分隔)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
brute force: use root.left and root.right to find all the nodes in tree, and record them

optimized: cause level order -> use BFS -> use queue to append nodes level by level, if root.left or root.right exist, 
append it to queue
variables set: level(record every level nodes), res(all levels final result), queue(append nodes follow their level by using root.left 
and root.right; pop nodes level by level)
height: O(logn ~ n)
edge case: root == None, return empty list
time: O(n)
space: O(n)
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            res.append(level)
        
        return res
            
            

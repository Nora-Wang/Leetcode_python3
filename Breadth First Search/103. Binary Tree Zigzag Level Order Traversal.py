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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        
        result = []
        flag = True
        
        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
            if flag:
                level.reverse()
            flag = not flag
            result.append(level)
        
        return result

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
brute force: utilize the count of root.left and root.right to record level by level, and use a variable(True or False) to deside when need to invert the level

optinized: traverse the tree level by level -> BFS -> use queue
append node if node.left or node.right exist, use a for loop to pop node level by level
use a variable(True or False) ot deside when to invert the level

variables set: queue(for BFS), res(final result), level(record nodes level by level), invert(boolean, deside when reverse level)

height: O(logn ~ n)
time: O(n)
space: O(n)
edge case: root is None, return empty list
'''


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        invert = False
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if invert:
                level.reverse()
            
            res.append(level)
            invert = not invert
        
        return res
                    

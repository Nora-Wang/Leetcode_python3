Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.



注意题目意思是root到最近的叶节点的距离,因此只要当前node是一个叶节点,直接返回level即可

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.bfs(root)
    
    def bfs(self, root):
        queue = collections.deque([root])
        
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return level
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
brute force:
#Recursion(DFS)
1. base case: root is None, return; curt root is leaf, use curt depth with global variable, choose a min one
2. recursion rule: walk through all paths in the tree find the min-depth
3. return value: global variable
time: O(n^2)
space: O(1)

optimized:
#BFS
1. analyze: use a queue to record the nodes; use a for loop to separate and count level; if root.left or root.right is the leaf node, return curt depth; if one of left/right is None, not append it to the queue
2. variable set: queue(BFS), depth(record level depth)
3. edge case: root is None, return 0
4. time: O(n), space: O(1)
'''

#Recursion(DFS)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.depth = float('inf')
        self.dfs(root, 1)
        
        return self.depth
    
    def dfs(self, root, level):
        if not root:
            return
        
        if not root.left and not root.right:
            self.depth = min(self.depth, level)
            return
        
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    

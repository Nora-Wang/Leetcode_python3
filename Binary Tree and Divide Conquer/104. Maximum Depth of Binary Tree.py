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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
brute force: walk through all path one by one from root to leaf, compare depth
time: O(n^2), space: O(1)

optimized: 
BFS
1. Analyze: traverse the tree level by level to find the depthest level -> use BFS (if root.left or root.right exist, append them to queue; utilize a for loop to saperate level)
2. variables set: queue(for BFS), count(count the depth)
3. edge case: root is None, count = 0, return
4. time:O(n), space: O(1)

Divide and conquer
1. Analyze:
1.1 base case: root is None, depth is 0
1.2. recurtion rule: get the depthest length for root.left node and root.right node, get the max of two length and plus 1, that's the curt root's depthest length
1.3. return value: return the curt root's depthest length

2.variables set: left(the depthest length for root.left node), right(the depthest length for root.right node)

3.edge case: root is None, depth is 0
4.time: O(n), space:O(1)
'''


#BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        count = 0
        
        while queue:
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return count
    
    
#Divide and Conquer
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

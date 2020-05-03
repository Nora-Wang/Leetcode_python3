Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
level traverse -> BFS -> queue
final res append the last node in every level. the last node is last end node of the level for loop.

time: O(logn ~ n), space: O(logn ~ n)
'''


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(node.val)
            
        return res

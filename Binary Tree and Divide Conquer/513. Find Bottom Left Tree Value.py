Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1


# DFS
# Time O(n), Space O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.max_level = 1
        self.helper(root, 1)
        
        return self.res
    
    def helper(self, node, level):
        if not node:
            return
        
        if self.max_level < level:
            self.max_level = level
            self.res = node.val
        
        self.helper(node.left, level + 1)
        self.helper(node.right, level + 1)


# BFS
# Time O(n), Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        
        res = root.val
        while queue:
            res = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

# BFS 进阶版
# 每一层，从右往左的去遍历，这样最后一个pop出的node一定是最后一层的最左边的node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        res = root.val
        
        while queue:
            node = queue.popleft()
            res = node.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return res

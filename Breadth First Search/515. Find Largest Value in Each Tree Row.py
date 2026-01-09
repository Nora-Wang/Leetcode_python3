Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1


# 01/09/2026
# BFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            cur = -float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()

                if cur < node.val:
                    cur = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            res.append(cur)
        
        return res

# DFS
# HashMap
# Time O(n), Space O(logn ~ n)
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 这里不能用collections.defaultdict，因为这个在initial的时候，会直接赋值为0，而题目里-231 <= Node.val <= 231 - 1
        self.record = {}
        self.helper(root, 0)

        return [value for _,value in sorted(self.record.items())]
    
    def helper(self, node, depth):
        if not node:
            return
        
        self.record[depth] = max(node.val, self.record[depth]) if depth in self.record else node.val

        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)

# List Index
# Time O(n), Space O(1)
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, 0, res)

        return res

    def helper(self, root, depth, res):
        if not root:
            return
        
        if depth == len(res):
            res.append(root.val)
        
        if root.val > res[depth]:
            res[depth] = root.val
        
        self.helper(root.left, depth + 1, res)
        self.helper(root.right, depth + 1, res)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val > max_val:
                    max_val = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(max_val)
        
        return res
        
        
        
        
# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        self.dfs(root, res, 1)
        
        return res
    
    def dfs(self, root, res, level):
        if not root:
            return
        
        while level > len(res):
            res.append(float('-inf'))
        res[level - 1] = max(res[level - 1], root.val)
        
        self.dfs(root.left, res, level + 1)
        self.dfs(root.right, res, level + 1)

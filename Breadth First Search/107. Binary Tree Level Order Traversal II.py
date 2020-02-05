题目：
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

思路：
同107，最后result.reverse()一下就行
需要注意的是不能这样写：return result.reverse()，因为result.reverse()是一个使result翻转的函数调用，其本身是不返回值的，这样的结果是[]

注意循环使用for _ in range(len_level):

code: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return[]
        
        return self.bfs(root)
    
    def bfs(self, root):
        queue = collections.deque([root])
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result[::-1]

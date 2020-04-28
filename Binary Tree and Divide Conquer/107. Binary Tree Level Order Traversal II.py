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
同107，最后reverse一下就行
需要注意的是不能这样写：return result.reverse()，因为result.reverse()是一个使result翻转的函数调用，其本身是不返回值的，这样的结果是[]
但可以写成return reversed(result)/ result[::-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
brute force:
use root.left and root.right to find the last level, and then find the second last level...
time: O(n^2), space: O(n)

optimized:
1. analyze: level traversal -> BFS, if left/right exist, append it to queue
2. variable set: queue(BFS), level(record nodes for curt level), stack_u_b(record levels from up to bottom)
3. edge case: root is None, return empty list
4. time: O(n), space: O(n)
'''


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        stack_u_b = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            stack_u_b.append(level)
        
        #return stack_u_b[::-1]
        return reversed(stack_u_b)

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

# 2026/01/14
# BFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque([(p, q)])

        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            if not self.valid(p, q):
                return False
            
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        
        return True
    
    def valid(self, p, q):
        if not p or not q:
            return False
        
        return p.val == q.val

# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = collections.deque([p])
        queue_q = collections.deque([q])
        
        while queue_p and queue_q:
            p, q = queue_p.popleft(), queue_q.popleft()

            # 这里一定要先判断p和q不为None，否则在后续queue.add(None)，以及p/q.left会throw exception
            if not p and not q:
                continue
            if not self.isSame(p, q):
                return False
            
            queue_p.append(p.left)
            queue_p.append(p.right)
            queue_q.append(q.left)
            queue_q.append(q.right)
        
        return not queue_p and not queue_q
    
    def isSame(self, p, q):
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return True
            


#这道题不能用
#return p == q
#因为p和q只是一个指向地址而已,并不代表两棵树本身
'''
for every level, the root, left, right should all same
return: for curt root, is it same?
end case:
1. both are None -> True
2. one of the node is None -> False
3. not equal -> False
4. equal -> depends on curt node's left and right subtree's results

!!edge case: both p and q are None
'''

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

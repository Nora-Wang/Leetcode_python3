In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


# 2026/01/12
# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False
        
        self.x_depth, self.y_depth, self.x_parent, self.y_parent = None, None, None, None

        self.helper(root.left, 1, x, y, root)
        self.helper(root.right, 1, x, y, root)

        return self.x_depth and self.y_depth and self.x_depth == self.y_depth and self.x_parent != self.y_parent

    def helper(self, node, depth, x, y, parent):
        if not node:
            return
        
        if self.x_depth and self.y_depth:
            return

        if node.val == x:
            self.x_depth = depth
            self.x_parent = parent
        if node.val == y:
            self.y_depth = depth
            self.y_parent = parent
        
        self.helper(node.left, depth + 1, x, y, node)
        self.helper(node.right, depth + 1, x, y, node)

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False

        queue = collections.deque()
        if root.left:
            queue.append((root.left, root))
        if root.right:
            queue.append((root.right, root))

        while queue:
            parent_x, parent_y = None, None
            for _ in range(len(queue)):
                node, parent = queue.popleft()

                if node.val == x:
                    parent_x = parent
                if node.val == y:
                    parent_y = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            if parent_x and parent_y and parent_x != parent_y:
                return True
        
        return False









code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([root])
        flag_x, flag_y = False, False
        
        while queue:
            #层级遍历
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val == x:
                    flag_x = True
                if node.val == y:
                    flag_y = True
                
                #保证x和y的parent不同
                if node.left and node.right:
                    #这里不能做加法/乘法之类的比较,因为可能存在情况:x=1,y=3,1+3 == 2+2
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #一层遍历结束后,发现x和y存在于同一层中,则返回True
            if flag_x and flag_y:
                return True
            
            #发现x或y单独存在于一层,则说明x和y不是cousin
            if (flag_x and not flag_y) or (not flag_x and flag_y):
                return False
                
    
        
        

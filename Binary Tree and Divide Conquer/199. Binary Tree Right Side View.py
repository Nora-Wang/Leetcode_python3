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
  

哇，这题很有意思啊。
主体思路就是level order traverse。
常规直接用BFS，但其实还有4种DFS解法。
DFS主要分为recursion和stack两种类型，每种又能分为从左到右的遍历还是从右到左的遍历，区别主要是空间复杂度。
BFS无论从左到右的遍历还是从右到左的遍历都是O(1)的空间，所以无所谓左右。


  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#DFS Version
'''
DFS Version
1. use recursion
use recursion to level order traverse the tree, utilize depth
1.1 really level order (from left to right), which means result is the last element in the record; use a list1[list2] to 
record every level, index of list1 means the depth, list2 is the nodes in curt depth
time: O(n), space: O(n)
1.2 revised level order traverse, which means the result is the first element in the record; 
if curt depth == len(record), which means curt root is the first node in the new depth(the most right one)
time: O(n), space: O(1)

2. use stack
use stack to process the dfs for level order traverse, utilize depth
2.1 really level order...
2.2 revised level order...
'''
#DFS recursion 1.1
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0)
        
        return [level[-1] for level in self.res]
    
    def dfs(self, root, depth):
        if not root:
            return
        
        if depth >= len(self.res):
            self.res.append([])
        
        self.res[depth].append(root.val)
        
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

#DFS recursion 1.2 revised
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0)
        
        return self.res
    
    def dfs(self, root, depth):
        if not root:
            return
        
        if depth == len(self.res):
            self.res.append(root.val)
        
        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)

#DFS + Stack 1.1
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [(root, 0)]
        res = []
        
        while stack:
            node, depth = stack.pop()
            
            if depth == len(res):
                res.append([])
            
            res[depth].append(node.val)
            
            #注意stack的特性，先进后出；这里要先append right，这样在stack pop的时候才会先pop出left，最后append进res的顺序才是left->right
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
            
        
        return [level[-1] for level in res]

#DFS + Stack 1.2 revised
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [(root, 0)]
        res = []
        
        while stack:
            node, depth = stack.pop()
            
            if depth == len(res):
                res.append(node.val)
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return res



#BFS Version
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

# 先右再左的写法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if level == len(res):
                    res.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            
            level += 1
    
        return res

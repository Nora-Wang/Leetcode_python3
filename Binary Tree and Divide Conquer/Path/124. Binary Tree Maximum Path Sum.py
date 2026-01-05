题目：
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

# 01/05/2026
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val / float('-inf')
        self.helper(root)

        return self.result

    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        # Tricky 1: 这里在做比较的时候一定要带上root.val其本身
        self.result = max(self.result, root.val, root.val + left, root.val + right, root.val + left + right)

        # Tricky 2: 这里由于是Divide and Concur回到上一层去，那么必须带上当前的root.val
        return max(root.val + left, root.val + right, root.val)

        


       
# 1/19/21
# time: O(n), space: O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 这里初始化直接设为root.val即可
        self.res = root.val
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.res = max(self.res, root.val + left, root.val + right, root.val + left + right, root.val)
        
        # 这里的写法导致end case可以return 0
        # 因为这是一个path，因此要想将上面的node与下面的node连起来，就一定要将root算在内；另外，需要考虑全员负数的情况
        return root.val + max(left, right, 0)
       
       
       
       
       
       
       
       
       
       
       
# 12/07/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
max path sum:
1. left + root + right
2. root + left
3. root + right
4. root
every recursion level renew self.res
at least one node -> return max(left + root, right + root, root)
from down to top -> divide and conquer

time: O(n), space: O(n)
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        # edge case: [-3] -> cannot return 0, because the max sum could be negative
        if not root:
            return float('-inf')
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.res = max(self.res, left + root.val + right, root.val + left, root.val + right, root.val)
        
        return max(root.val, left + root.val, right + root.val)
       
       
       

#05/01/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
brute force
find all paths in the tree
time?? space: O(1)

optimize
use divide and conquer
1. definition
maxPathSum(root)
2. rules
use gloable variable to record the max sum -> self.max_sum
compare (self.max_sum, left + root, right + root, root, left + right + root) to get a max sum for curt root -> new self.max_sum
3. return 
max(left + root, right + root, root, 0)
4. base case
not root, return 0

time: O(n), space: O(1)
'''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_sum = -float('inf')
        self.helper(root)
        
        return self.max_sum
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.max_sum = max(self.max_sum, left + root.val, right + root.val, root.val, left + right + root.val)
        
        return max(left + root.val, right + root.val, root.val, 0)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
code:
Version 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        #在root这个点得到最大值,与5个值做比较
        #1. 与self.res自己做比较
        #2. 与左边+root做比较,即左边线
        #3. 与右边+root做比较,即右边线
        #4. 与全部做比较,即从左边线到右边线的所有和
        #5. 与root自己比较,因为存在左右两条边线的值都为负数的情况,这样返回root的值才是当前最大
        self.res = max(self.res, left + right + root.val, left + root.val, right + root.val, root.val)
        
        #返回值相当于又要往上走,因此只用返回一条边线即可,因为存在左右两条边线的值都为负数的情况,因此还得与root自己比较
        return max(left + root.val, right + root.val, root.val)
       
       
       
       
       
       
       
       
Version 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left_max = self.helper(root.left)
        right_max = self.helper(root.right)
        
        
        self.res = max(self.res, left_max + right_max + root.val)
        
        curt = max(left_max, right_max) + root.val
        
        return max(curt, 0)

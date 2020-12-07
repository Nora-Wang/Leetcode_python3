You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

# 12/07/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
path situation:
1. left + root
2. right + root
3. left + right + root
4. root

need left and right sum -> divide and conquer
return: one path with the min_diff between (root, left + root, right + root) and sum

time: O(n), space: O(n)
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        self.count = 0
        self.helper(root, 0, sum)
        
        return self.count
    
    def helper(self, root, temp, sum):
        if not root:
            return 0
        
        left = self.helper(root.left, temp + root.val, sum)
        right = self.helper(root.right, temp + root.val, sum)
        
        if left + root.val == sum:
            self.count += 1
        if right + root.val == sum:
            self.count += 1
        if left + right + root.val == sum:
            self.count += 1
        if root.val == sum:
            self.count += 1
        
        min_diff = min(abs(root.val - sum), abs(left + root.val - sum), abs(root.val + right - sum))
        
        if min_diff == abs(root.val - sum):
            return root.val
        elif min_diff == abs(left + root.val - sum):
            return left + root.val
        else:
            return root.val + right
        
        






code:
#两个DFS function
'''
must go downwards -> dfs -> for every node in the tree, do a dfs to count the sum -> use two dfs, one for traversing 
every node in the tree, another for count curt node's downwards sum

time: O(nlogn), space: O(n)
'''
时间复杂度： T(N) = 2T(N/2) + O(N)，根据Master公式，可知 复杂度为O(NlogN)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.dfs(root, sum)
        
        return self.res
    
    def dfs(self, root, sum):
        if not root:
            return
        
        self.helper(root, 0, sum)
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        
    def helper(self, root, curt, sum):
        if not root:
            return
        
        if curt + root.val == sum:
            self.res += 1
        
        self.helper(root.left, curt + root.val, sum)
        self.helper(root.right, curt + root.val, sum)
        
        
        
#用一个变量来作为是否连续的记录
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.dfs(root, 0, sum, False)
        
        return self.res
    
    def dfs(self, root, curt, sum, consecutive):
        if not root:
            return
        
        if curt + root.val == sum:
            self.res += 1
            
        if not consecutive:
            self.dfs(root.left, 0, sum, False)
            self.dfs(root.right, 0, sum, False)
        
        self.dfs(root.left, curt + root.val, sum, True)
        self.dfs(root.right, curt + root.val, sum, True)

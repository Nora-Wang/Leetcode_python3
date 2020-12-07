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
#两个DFS function
'''
must go downwards -> dfs -> for every node in the tree, do a dfs to count the sum -> use two dfs, one for traversing 
every node in the tree, another for count curt node's downwards sum

time: O(nlogn), space: O(n)
'''
时间复杂度： T(N) = 2T(N/2) + O(N)，根据Master公式，可知 复杂度为O(NlogN)
# 这里之所以有logn是因为每次得重新计算path sum -> optimal的方法是用一个memo记录path sum，这样若node在memo中，则直接得到path sum -> time: O(n)

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

# Optimal with memorization






# 错误的做法，原因如下:
# eg: [5,4,8,11,null,13,4,7,2,null,null,5,1], 22
#        5
#      /  \
#     4    8
#    /    / \
#   11   13  4
#  / \      / \
# 7   2    5   1
# 1. 在处理self.count时，这里用4个situation来分类，一旦==sum，则count++。这样做是有问题的。
#    例如上面的path [4,11,7] = 22: root 4的left+root可使count++，但同时root 4的left+root+right也可使count++
# 2. return min_diff也有问题
#    例如path [5,8,4,1], 对于8来说，left 13与target 22的diff比right 5更小，因此最后不能得到该path
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

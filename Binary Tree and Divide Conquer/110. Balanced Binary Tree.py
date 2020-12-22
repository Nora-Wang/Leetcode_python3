题目：
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.


brute force:
utilize root.left and root.right to count the left/right subtrees depth for every node
time: O(n^2), space: O(n)

optimized:
    
Solution 1: top-down
end case: not root -> return 0 (height)
left_height
right_height
return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)

time: O(nlogn), space: O(n)
for time: there a n nodes in the tree need to varify is_balanced. 
          the height for the whole tree is logn -> need logn time to get the height for every node 

Solution 2: down-top
use Divide and Conquer
1. base case
root is None, return 0(depth), True(is balanced)
2. Recursion rule
count root.left depth and root.right depth, compare them(whether balanced)
compare situation: root.left is not balanced; root.right is not balanced; curt root is not balanced
3. input
root
4. return value
max (root.left depth, root.right depth) + 1, whether curt root is balanced

time: O(n), space: O(1)
# Solution 1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def get_height(self, root):
        if not root:
            return 0
        
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced, _ = self.helper(root)
        
        return is_balanced
    
    def helper(self, root):
        if not root:
            return True, 0
        
        l_b, l_h = self.helper(root.left)
        r_b, r_h = self.helper(root.right)
        
        #left or right is not balanced
        if not l_b or not r_b:
            return False, max(l_h, r_h) + 1
        
        #root is not balanced
        if abs(l_h - r_h) > 1:
            return False, max(l_h, r_h) + 1
        
        return True, max(l_h, r_h) + 1

# Solution 2 simplify
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res, _ = self.helper(root)
        return res
    
    def helper(self, root):
        if not root:
            return True, 0
        
        left, l_depth = self.helper(root.left)
        right, r_depth = self.helper(root.right)
        
        return left and right and abs(l_depth - r_depth) <= 1, max(r_depth, l_depth) + 1
        
        
    
    
    
    
    
    
    
    
    



推荐用version1，因为定义了IsBalanced，代码清晰，更好理解
version2用-1做标记，容易出错


1. Version九章
divide and conquer
用两个值分别代表深度和平衡性
自下而上递归判断每个节点是否平衡。若平衡将当前节点高度返回，供父节点判断;否则该树一定不平衡。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, isbalanced = self.maxdepth(root)
        
        return isbalanced
    
    def maxdepth(self, root):
        if not root:
            return 0, True
        
        left_depth, left_isbalanced = self.maxdepth(root.left)
        if not left_isbalanced:
            return 0, False
        
        right_depth, right_isbalanced = self.maxdepth(root.right)
        if not right_isbalanced:
            return 0, False
        
        return max(left_depth, right_depth) + 1, abs(left_depth - right_depth) <= 1
        

        
        
        
2.Simple Version
思想：divide and conquer
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    #利用dfs函数的返回值作为标志，若为-1则说明不平衡，反之则平衡
    def dfs(self, root):
        if not root:
            return 0
            
        #divide
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        #conquer
        #左子树或右子树不平衡时
        if left == -1 or right == -1:
            return -1
        
        #左右子树高度差>1时
        if abs(left - right) > 1:
            return -1
            
        #返回该root的高度，以便于后续node的高度计算（即下一层直接+1）
        return max(left, right) + 1
    
    def isBalanced(self, root):
        if self.dfs(root) == -1:
             return False
        return True
        
        

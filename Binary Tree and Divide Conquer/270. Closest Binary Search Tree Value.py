Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

    
    
#05/10/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
similar with valid BST
utilize BST property, use upper and lower bound to record, in the end, conpare the diff between upper/lower and target, get the min_diff one

rule:
root.val > target -> upper = root.val, go to root.left
root.val < target -> lower = root.val, go to root.right

end case:
while root

edge case:
root = target, return

time: depends on depth of the tree(O(logn) ~ O(n)), space: O(1)
'''

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        lower, upper = -float('inf'), float('inf')
        
        while root:
            if root.val > target:
                upper = min(root.val, upper)
                root = root.left
            else:
                lower = max(root.val, lower)
                root = root.right
                
        return upper if upper - target < target - lower else lower
    
    
'''
utilize the property of BST
use diff(abs(curt root.val - target)) and res(curt closest root.val) to record
from root to leaf, recursion to find res

rules:
target > curt root -> go to root.right, renew diff and res
target == curt root -> return root.val
target < curt root -> go to root.left, renew diff and res

time: depends on the depth of tree(logn ~ n), space: O(1)
'''

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.diff, self.res = float('inf'), root.val
        
        self.helper(root, target)
        
        return self.res
    
    def helper(self, root, target):
        if not root:
            return
        
        if root.val == target:
            self.res = root.val
            self.diff = 0
            return
        
        curt_diff = abs(target - root.val)
        if curt_diff < self.diff:
            self.diff = curt_diff
            self.res = root.val
        
        if root.val < target:
            self.helper(root.right, target)
        else:
            self.helper(root.left, target)
            
            

思路：
如果当前root值比target大，就暂且把这个root值当成上限upper，然后往左边走root = root.left
如果当前root值比target小，就暂且把这个root值当成下限lower，然后往右边走root = root.right
左右摇摆着走，知道发现两个最接近target的值，由于是inplace的更新上下限，而且不递归，所以没有额外的空间损耗
O(h) time and O(1) space


code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        
        upper = root.val
        lower = root.val
        
        while root:
            if target > root.val:
                lower = root.val
                root = root.right
            elif target < root.val:
                upper = root.val
                root = root.left
            else:
                return root.val
            
        if abs(upper - target) > abs(lower - target):
            return lower
        else:
            return upper
            
        
        

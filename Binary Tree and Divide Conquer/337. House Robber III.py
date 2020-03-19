The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.helper(root, {})
    
    def helper(self, root, memo):
        if not root:
            return 0
        
        if root in memo:
            return memo[root]
        
        #case 1
        res1 = self.helper(root.left, memo) + self.helper(root.right, memo)
        
        #case 2
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left.left, memo) + self.helper(root.left.right, memo)
        if root.right:
            right = self.helper(root.right.left, memo) + self.helper(root.right.right, memo)
        res2 = root.val + left + right
        
        memo[root] = max(res1, res2)
        
        return memo[root]
        
        

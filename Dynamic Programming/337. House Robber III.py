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

     
divide and conquer + dynamic programming

利用path sum的思路进行divide and conquer，在conquer的时候利用dp思路得到当前node的值
     
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
对于每个点
dp[0]: not rob
dp[1]: rob

#如果当前点not rob，则当前点conquer的时候应该返回left的最大值 + right的最大值
dp[0] = max(dp[left][0], dp[left][1]) + max(dp[right][0], dp[right][1])
#如果当前点rob，则说明left和right只能not rob
dp[1] = max(dp[left][0], dp[right][0]) + curt node.val

'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = self.helper(root)
        
        return max(res[0], res[1])
    
    def helper(self, root):
        if not root:
            return [0, 0]
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = left[0] + right[0] + root.val
        
        return res

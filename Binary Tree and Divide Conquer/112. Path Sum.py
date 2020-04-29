Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
walk through all paths in the tree from root to leaf -> DFS
1. input/define: root, target, prev_sum
2. base case: 
root is None(only exist in one case: root/root.left exist, but root.right not exist, then judge root.right node), 
return False(curt root.right is not a leaf); 
root is a leaf, judge curt sum + root.val == target
3. recursion: judge root.left or root.right have a path that the sum equal to target
4. return: True or False for curt_sum = prev_sum + curt root.val == target

optimized:if all the nodes value are positive
if curt sum > sum, return directly

edge case: if root is None, return False

Time: O(n)
Space: O(1)????解释：
~~~~~~~~~~~~~~~~~~~~~~
Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, 
the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be  O(N). 
But in the best case (the tree is completely balanced), the height of the tree would be log(N). 
Therefore, the space complexity in this case would be O(log(N)). 

'''

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        return self.dfs(root, sum, 0)
    
    def dfs(self, root, target, curt):
        if not root:
            return False
        
        if not root.left and not root.right:
            return curt + root.val == target
        
        return self.dfs(root.left, target, curt + root.val) or self.dfs(root.right, target, curt + root.val)

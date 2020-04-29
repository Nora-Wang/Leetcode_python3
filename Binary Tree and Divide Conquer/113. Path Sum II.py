Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Brute force
walk through all paths one by one
time: O(n^2), space: O(logn ~ n)(not include result space)


Optimize:
use DFS for backtracking
1. recursion input/definition
self.result
dfs(root, prev_sum, temp, target_sum)

2. recursion rules
root.left/root.right, prev_sum + root.val, temp.append(root.val), target_sum

3. return value
append the valide temp to the final result(self.result), return final result

4. base case
root is None: return
root is leaf: judge prev_sum + root.val == target sum -> append temp to self.result

time: O(n^2)个人觉得是O(n)???
Time Complexity: O(N^2)where N are the number of nodes in a tree. 
In the worst case, we could have a complete binary tree and if that is the case, then there would be N/2 leafs. 
For every leaf, we perform a potential O(N) operation of copying over the pathNodes nodes to a new list to be added to the 
final pathsList. Hence, the complexity in the worst case could be.

space: O(logn ~ n) the height of the tree
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0, [], sum)
        
        return self.res
    
    def dfs(self, root, prev_sum, temp, target):
        if not root:
            return
        
        if not root.left and not root.right:
            if prev_sum + root.val == target:
                self.res.append(list(temp) + [root.val])
            return
        
        temp.append(root.val)
        self.dfs(root.left, prev_sum + root.val, temp, target)
        self.dfs(root.right, prev_sum + root.val, temp, target)
        temp.pop()



code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(root, [], sum, results)
        
        return results
    
    def dfs(self, root, path, target, results):
        if not root:
            return
        
        path.append(root.val)
        
        if target == root.val and not root.left and not root.right:
            return results.append(list(path))
        
        self.dfs(root.left, list(path), target - root.val, results)
        self.dfs(root.right, list(path), target - root.val, results)
        

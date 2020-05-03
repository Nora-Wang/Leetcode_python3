Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
#recursion solution
use recursion to traverse every node in the tree, count + 1, return count

#BFS solution
count nodes -> traverse all nodes in the tree -> level traverse -> BFS

#DFS solution
complete Tree -> just count the last level nodes + 2^(depth - 1), the last level nodes means the leaf -> use DFS the count the number of leaves in the tree

above three brute force solution: time O(n), space O(n)

#optimize
use binary search
'''

#brute force
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
        
        
#binary search
referral https://leetcode.wang/leetcode-222-Count-Complete-Tree-Nodes.html


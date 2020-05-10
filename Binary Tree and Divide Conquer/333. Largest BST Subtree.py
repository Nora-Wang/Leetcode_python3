Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?


code:
'''
a valid BST, which means both left and right subtree are BST and match the rules that left_upper_bound < root < right_lower_bound

use divide and conquer
1. rules: varify whether curt root is a valid BST
both left and right subtrees are BST;
left_upper_bound < root < right_lower_bound;
-> True
if True, renew the self.res

2. return
is_BST(True/False)
curt_size(if curt root is BST, left + right + 1; else max(left, right) + 1)
curt_upper_bound(compare with right_upper bound and root.val)
curt_lower_bount(compare with left_lower bound and root.val)

3. edge case
not root, return True, 0(size), -float('inf')(upper), float('inf')(lower)

time: O(n), space: O(1)
'''

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return True, 0, -float('inf'), float('inf')
        
        left_is_BST, left_size, left_upper, left_lower = self.helper(root.left)
        right_is_BST, right_size, right_upper, right_lower = self.helper(root.right)
        
        curt_BST = left_is_BST and right_is_BST and left_upper < root.val < right_lower
        curt_size = left_size + right_size + 1 if curt_BST else max(left_size, right_size) + 1
        curt_upper = max(right_upper, root.val)
        curt_lower = min(left_lower, root.val)
        
        if curt_BST:
            self.res = max(curt_size, self.res)
        return curt_BST, curt_size, curt_upper, curt_lower

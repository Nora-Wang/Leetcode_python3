Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example

Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.


思路：divide and conquer + traverse
找出左右子树的sum、左右子树minsum及其root；计算root的sum，与左右子树的minsum做比较，返回当前sum，比较后的minsum及其root

注意点：返回值的选取
left_min_root, left_sum, left_minsum

code:
Version 1: 不使用全局变量,纯divide and conquer
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        root,_,_ = self.minsum(root)
        
        return root
        
    def minsum(self, root):
        if not root:
            return root, 0, sys.maxsize

        #左边最小sum子树的root，左边的sum，左边最小sum
        left_min_root, left_sum, left_minsum= self.minsum(root.left)
        right_min_root, right_sum, right_minsum= self.minsum(root.right)
        
        cur_sum = left_sum + right_sum + root.val
        
        min_sum = min(left_minsum, right_minsum, cur_sum)
        
        if min_sum == left_minsum:
            #注意这里返回的是cur_sum，这样后续才能继续计算当前root的sum
            return left_min_root, cur_sum, left_minsum
        if min_sum == right_minsum:
            return right_min_root, cur_sum, right_minsum
            
        return root, cur_sum, cur_sum


Version 2:使用全局变量,divide and conquer + traversal
     """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        self.subtree = None
        self.sum_record = sys.maxsize
        self.minsum(root)
        
        return self.subtree
        
    def minsum(self, root):
        if not root:
            return 0
            
        left_sum = self.minsum(root.left)
        right_sum = self.minsum(root.right)
        
        root_sum = left_sum + right_sum + root.val
        
        if self.sum_record > root_sum:
            self.sum_record = root_sum
            self.subtree = root
            
        return root_sum

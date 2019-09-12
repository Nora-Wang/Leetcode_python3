题目：
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.





主要思路：
DFS Divide and Conquer solution：左右两边返回后，处理当前，然后比较大小。
关键是最后的返回值里，要有计算出的最大平均值，root，sum，size
定义sum和size是因为计算平均值时需要同时使用这两个值；若是minimum subtree，只需要sum，root就足够

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
    @return: the root of the maximum average of subtree
    # """
    def findSubtree2(self, root):
        avg, root,_,_ = self.dfs(root)
        return root
        
    def dfs(self, root):
        
        if not root:
            return -sys.maxsize, root, 0, 0
        
        left_avg, left_root, left_sum, left_size = self.dfs(root.left)
        right_avg, right_root, right_sum, right_size = self.dfs(root.right)
        
        size = left_size + right_size + 1
        sum = left_sum + right_sum + 1
        avg = sum / size
        
        max_avg = max(avg, left_avg, right_avg)
        
        if(left_avg == max_avg):
            return left_avg, left_root, left_sum, left_size
        
        if(right_avg == max_avg):
            return right_avg, right_root, right_sum, right_size
           
        return max_avg, root, sum, size

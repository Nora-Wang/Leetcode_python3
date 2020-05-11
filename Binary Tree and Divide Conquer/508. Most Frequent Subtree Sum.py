Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.


#similar with 501


code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. count all subtree's sum, record them to a list
use divide and conquer
for every node, get the left and right subtree's sum, calculate the sum of curt node, node.val + left + right, return curt sum to its parent node

2. turn the list to a hashtable, find the highest frequency one

'''
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        record = []
        self.helper(root, record)
        
        record = collections.Counter(record)
        
        most_fre = max(record.values())
        
        res = []
        for k, v in record.items():
            if v == most_fre:
                res.append(k)
        
        return res
    
    def helper(self, root, record):
        if not root:
            return 0
        
        left = self.helper(root.left, record)
        right = self.helper(root.right, record)
        
        curt_sum = left + right + root.val
        
        record.append(curt_sum)
        
        return curt_sum

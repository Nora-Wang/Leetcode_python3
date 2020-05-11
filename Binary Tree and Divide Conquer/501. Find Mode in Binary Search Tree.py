Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).




code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. brute force
hashtable solution
cause need to count the frequency, so just traverse every node in the tree, count the frequency in a hashtable{node.val:frequency}, compare the frequency in the hashtable to get the highest frequent node list
time: O(n), space: O(n)
'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        record = self.get_nodes(root)
        record = collections.Counter(record)
        
        most_fre = max(record.values())
        
        res = []
        for key, value in record.items():
            if value == most_fre:
                res.append(key)
        
        return res
    
    def get_nodes(self, root):
        record = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                record.append(root.val)
                root = root.right
        
        return record

'''
2. optimize
utilize BST property -> inorder traverse the tree

use self.res to record the mode(s) value, use self.fre to record the highest frequency

use prev to record prev node's value, use curt to record curt_count
if curt_count == self.fre -> append curt node to self.res
if curt_count > self.fre -> renew self.res and self.fre

time: O(n), space: O(1)

'''

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.res = []
        self.fre = 0
        self.prev = None
        self.curt_count = 1
        
        self.inorder(root)
        
        return self.res
    
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        
        self.curt_count = 1 if self.prev != root.val else 1 + self.curt_count
        
        if self.curt_count > self.fre:
            self.fre = self.curt_count
            self.res = [root.val]
        elif self.curt_count == self.fre:
            self.res.append(root.val)
            
        self.prev = root.val
            
        self.inorder(root.right)

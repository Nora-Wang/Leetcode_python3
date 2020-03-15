Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.


code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = self.inorder(root)
        
        new_root = self.helper(nodes)
        
        return new_root
    
    def helper(self, nodes):
        if not len(nodes):
            return None
        
        start = 0
        end = len(nodes) - 1
        mid = (start + end) // 2
        
        root = TreeNode(nodes[mid])
        root.left = self.helper(nodes[:mid])
        root.right = self.helper(nodes[mid + 1:])
        
        return root
        
        
    def inorder(self, root):
        if not root:
            return []
        
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        
        res = []
        res.extend(left)
        res.append(root.val)
        res.extend(right)
        
        return res
    
    

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.




#Version 自写
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        self.res = None
        self.prev = None
        self.helper(root, p)
        
        return self.res
    
    def helper(self, root, p):
        if not root:
            return
        
        self.helper(root.left, p)
        
        if self.prev and self.prev.val == p.val:
            self.res = root
            #为了避免后续可能还会出现self.prev.val == p.val,所以要更新一下self.prev
            self.prev = None
            return
        self.prev = root
        
        self.helper(root.right, p)
        
        







思路:参考二分法，考虑p和root之间的关系(p为给定的节点,要找到p节点的后继)
两种情况:
1. root的值 =< p的值 答案就在右子树中
2. root的值 > p的值 答案有两个备选: 
a) 就是root
b) 左子树中找(如果找到就一定是它，因为左子树的中的元素都比根小)

code:
时间复杂度为O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        
        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        
        return root

       
       
Inorder倒过来用,用两个全局变量记录结果和前一个node
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.result = None
        self.prev = None
        
        self.helper(root, p)
        return self.result
    
    def helper(self, root, p):
        if not root or self.result:
            return
        
        self.helper(root.right, p)
        if root.val == p.val:
            self.result = self.prev
        
        self.prev = root
        self.helper(root.left, p)


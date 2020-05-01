题目：
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true


'''
brute force
utilize inorder. all the element in the tree, use a prev variable to compare it
time: O(n), space: O(1)

optimize
use divide and conquer
1. definition: helper(root, lower, upper)
set a lower bound and upper bound for curt tree's nodes, every time compare is curt node in the range(return True or False). 
for root.left part, root.val is the upper bound; for root.right part, root.val is the lower bound
2. rules: both left and right part are BST
3. base case: if not root, return True; node not in the range, return False
4. return: curt node is in the range?

time: O(n), space: O(1)
'''
 
 
code:
#optimize
#1 记录lower_bound和upper_bound,与当前root.val做比较
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, root, lower, upper):
        if not root:
            return True
        
        if root.val <= lower or root.val >= upper:
            return False
        
        return self.helper(root.left, lower, root.val) and self.helper(root.right, root.val, upper)
        

#brute force
#2 inorder divide and conquer,用一个全局变量来记录上一个node,然后将其与当前root.val做比较,因为BST是递增的
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = []
        prev = None
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev and prev.val >= root.val:
                    return False
                prev = root
                root = root.right
        
        return True


#divide and conquer
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lastnode = None
        return self.inorder(root)
    
    def inorder(self, root):
        if not root:
            return True
        
        left = self.inorder(root.left)
        
        if self.lastnode and self.lastnode.val >= root.val:
            return False
        self.lastnode = root
        
        right = self.inorder(root.right)
        
        #只有当左右子树都为BST时，整棵树才为BST
        if left and right:
            return True
 
 
 
 
 
 
 
 
 
 
 
 
########################################################################################################################
思路：
Version1：
仔细看题目，只存在比root大和比root小的情况，不存在等于的情况，因此可以直接利用BST的性质：若inorder traversal的结果是升序的，则为BST
注意这里inorder的时候若用traversal，需要与前一个node.val比较，若发现更小，则不是升序

1.1 traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inorder(root)
            
        
    def inorder(self, root):
        
        if not root:
            return True
        
        stark = []
        res = []
        
        while root or stark:
            while(root):
                stark.append(root)
                root = root.left
            root = stark.pop()
            if res == [] or root.val > res[-1]:
                res.append(root.val)
                root = root.right
            else:
                return False
            
        return True

1.2 divide and conquer
1.2.1
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
      #这里需要使用两个全局变量
      #一个用于记录上一个node，另一个用于记录是否为BST的结果
      #可以不用设置self.isBST,可将其作为inorder的结果，如1.2.2 version
        self.lastnode = None
        self.isBST = True
        self.inorder(root)
        return self.isBST
        
    def inorder(self, root):
        if not  root:
            return
        
        self.inorder(root.left)
        
        #需要先判断一下self.lastnode是否存在
        if self.lastnode and self.lastnode.val >= root.val:
            self.isBST = False
            return
        self.lastnode = root
        
        self.inorder(root.right)
            
1.2.2
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lastnode = None
        return self.inorder(root)
    
    def inorder(self, root):
        if not root:
            return True
        
        left = self.inorder(root.left)
        
        if self.lastnode and self.lastnode.val >= root.val:
            return False
        self.lastnode = root
        
        right = self.inorder(root.right)
        
        #只有当左右子树都为BST时，整棵树才为BST
        if left and right:
            return True
         
         
1.2.3
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        result = self.inorder(root)
#range注意取左不取右
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
                
        return True
        
    def inorder(self, root):
        if not  root:
            return []
            
        result = []
        
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        
        #inorder: left, root, right
        result += left
        result.append(root.val)
        result += right
        
        return result
            

       
Version2:
若用divide and conquer，则需要记录left_max和right_min，以此与root.val做比较,若出现left_max >= root.val or right_min <= root.val则为False

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return True
        self.left_max = -sys.maxsize
        self.right_min = sys.maxsize
        return self.traverse(root, self.left_max, self.right_min)
    
    def traverse(self, root, left_max, right_min):
        if not root:
            return True
        if left_max >= root.val or right_min <= root.val:
            return False
    ##注意return的写法，即当左右两边都满足条件才是True
        return self.traverse(root.left, left_max, root.val) and self.traverse(root.right, root.val, right_min)
    




题目：
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.





1. Version九章

Class ResultType
用ResultType类来记录depth和是否balanced
主要运用=是divide and conquer + traverse的思想

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#使用类来标记depth和isBalanced
class ResultType:
    def __init__(self, depth, IsBalanced):
        self.depth = depth
        self.IsBalanced = IsBalanced
        
class Solution:
    #直接返回在调用了MaxDepth函数后的root的IsBalanced
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.MaxDepth(root).IsBalanced
    
    def MaxDepth(self, root):
        #单节点情况
        if not root:
            return ResultType(0, True)
            
        #divide and conquer
        left = self.MaxDepth(root.left)
        right = self.MaxDepth(root.right)
        
        #当左节点或右节点不平衡时，以root为根的树也不是平衡二叉树
        if left.IsBalanced == False or right.IsBalanced == False:
            return ResultType(-1, False)
        
        #Balanced Binary Tree的定义：左右子树高度差小于等于1
        if abs(left.depth - right.depth) > 1:
            return ResultType(-1, False)
        
        #此处返回的是一个ResultType
        #能使用到这一return的node就说明此时的node是处于平衡的状态，需要记录其depth，以便于后续node求depth的时候可以直接+1
        return ResultType(max(left.depth, right.depth) + 1, True)
        
        
        
2.Simple Version
思想：divide and conquer
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    #利用dfs函数的返回值作为标志，若为-1则说明不平衡，反之则平衡
    def dfs(self, root):
        if not root:
            return 0
            
        #divide
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        #conquer
        #左子树或右子树不平衡时
        if left == -1 or right == -1:
            return -1
        
        #左右子树高度差>1时
        if abs(left - right) > 1:
            return -1
            
        #返回该root的高度，以便于后续node的高度计算（即下一层直接+1）
        return max(left, right) + 1
    
    def isBalanced(self, root):
        if self.dfs(root) == -1:
             return False
        return True
        
        

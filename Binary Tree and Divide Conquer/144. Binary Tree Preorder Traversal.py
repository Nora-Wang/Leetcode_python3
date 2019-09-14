题目：
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?


思路：
1.递归法recursive

首先遍历根节点，然后对其左节点做前序遍历，对其右节点做前序遍历。

递归三要素：

定义：要做什么事情。这道题就是先遍历父亲节点（将root加入到result[]中），然后左节点、右节点
拆分：差分成同样的问题，但规模变小。本题就是拆成左子树和右子树，对左子树和右字数分别做前序遍历
结束条件：规模变为最小的情况。本题为遇到空节点停止

递归可分为两种：traversal遍历和divide and conquer分治
区别：traversal的result是全局变量

主要掌握traversal和Non-recursive的方法

# Version 0: Traversal遍历 

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
#结束条件：本题为遇到空节点停止
        if root is None:
            return
####顺序是根左右
#定义：这道题就是先遍历父亲节点（将root加入到result[]中），然后左节点、右节点
        self.results.append(root.val)
#拆分本题就是拆成左子树和右子树，对左子树和右字数分别做前序遍历
        self.traverse(root.left)
        self.traverse(root.right)

      
#Version 1:divide and conquer分治

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return []
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
##注意left和right加入进result的写法，以及root的写法
        result.append(root.val)
        result += left
        result += right
        
        return result
        
        
        
2.非递归：迭代 Non-Recursive: Iteration

利用stack实现树的前序遍历，每次弹出栈顶元素，先后压入其右孩子和左孩子
    
# Version 2: Non-Recursion 

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """
    def preorderTraversal(self, root):
        if root is None:
            return []
        #根入栈
        stack = [root]
        preorder = []
      
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            
            #右节点入栈
            if node.right:
                stack.append(node.right)
            #左节点入栈
            if node.left:
                stack.append(node.left)
                  
        return preorder
   
######注意：先让右节点入栈，再让左节点入栈。
因为栈的特点是先进后出，栈每次pop的都是栈顶，所以当同存在左右节点时，需要先右后左，这样pop时就是先左后右，以满足preorder的要求

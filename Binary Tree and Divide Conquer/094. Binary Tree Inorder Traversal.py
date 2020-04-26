题目：
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?



solution 1: recursion
use a global variable to record the result (the different between recursion and divide and conquer)
1. Base case: if root == None -> return None
2. Recursive rule: if root.left != None, go to root.left; else, add root.val and then go to root.right
3. What value to return: use global variable to record curt root's traversal result 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.recursion(root)
      
        return self.result
   
    def recursion(self, root):
####顺序是左根右
        if not root:
            return
        self.recursion(root.left)
        self.result.append(root.val)
        self.recursion(root.right)

   
solution 2: divide and conquer
return a value to the next recursion
1. Base case: if root == None -> return None
2. Recursive rule: left = root.left's traversal result, right = root.right's traversal result
3. What value to return: return curt root's traversal result (list = [left + root.val + right])
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if not root:
            return []
            
        result = []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        #left, root, right
        result.extend(left)
        result.append(root.val)
        result.extend(right)
        
        return result
        

        
solution 3: interative
use stack
go to the most left node and use stack to record the path
if left nodes have been traversed, then from stack pop a node, add it to the result
analyze the node.right as a new round of root
#Che Li Version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res










Past:
思路：先把最左边全都加进stack，即此时的root就是inorder的first node。
     然后开始pop，每pop一次检查：1.右边为空就一直pop，相当于回到left node的root
                             2.不为空就到右边去，然后再一次while循环到右子树的第一个inorder node去，并全加进stack里
>       1
>     /   \
>    4     2
>   / \    /
>  5   6  3
   
   explain：
   1.stark里append了1，4，5（注意栈的先进后出）
   2.pop 5，此时root = 5，result.append(5),此时stark里还有1，4
   3.因为没有right，因此root = None，循环最外层的while以后，直接root = 4，此时stark里还有1
   4.result.append(4),此时有right，因此root = 6
   5.将6 append进stark，因为6没有left，所以直接pop，result.append(6)，root = None，然后就是pop 1

   
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stark = []
        result = []
            
        while root or stark:
            while root:
                stark.append(root)
                root = root.left
            root = stark.pop()
            result.append(root.val)
            root = root.right
        return result

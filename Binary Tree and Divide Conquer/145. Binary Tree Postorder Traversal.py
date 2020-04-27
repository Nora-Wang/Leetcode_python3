题目：
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?


   
   
#04/26/2020 Version
solution 1: Recursion
1. base case: if root is None, return directly
2. recusive rule: put root.left subtree's preorder to the result, put root.right subtree's preorder to the result, 
   put root to the result
3. return value: return directly. use a result list in funcion input, every function change it directly (avoid global variable)
time: O(n)
space: O(1)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        
        return res
    
    def helper(self, root, res):
        if not root:
            return
        
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

solution 2: divide and conquer
1. base case: if root is None, return empty list
2. recursion rule: get root.left subtree's postorder result, l_r; get root.right subtree's preorder result, r_r; 
   add l_r, r_r, root.val to the result
3. return value: return the root tree's postorder result
time: O(n)
space: O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        
        res = []
        res.extend(left)
        res.extend(right)
        res.append(root.val)
        
        return res


solution 3: iteratively
use stack, follow the rules of postorder: root.left -> root.right -> root
it's difficult to follow the postorder directly, but after invert the rules, the new rules(root -> root.right -> root.left) is
similar to preorder rules(root -> root.left -> root.right)
go to the most right one node, record the walk though path to stack, add the path to the result(root); pop a node from stack, 
analyze the node.left as a new root
end case: root = None and stack = None -> all the nodes in the tree have been visited
time: O(n)
space: O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        
        res.reverse()
        return res
   
   
   
   
   
   
   
   
   
   
   
   
   
   
1.Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.result = self.traverse(root)
        return self.result
    def traverse(self, root):
        
        if not root:
            return
###顺序是左右根
        self.traverse(root.left)
        self.traverse(root.right)
        self.result.append(root.val)
        return self.result
        
        
2.Non-recursive
#Che Li Version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = []
        res = []
        
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        
        return res[::-1]














终于找到一个简单易懂的Non-recursive方法
利用两个栈，在s1中按照根左右的顺序push进node，然后将右node pop出，再循环；即相当于将整个结果反着push进s2，这样s2 pop时的顺序就是postorder的顺序
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        s1 = [root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            
        while s2:
            result.append(s2.pop().val)
        return result

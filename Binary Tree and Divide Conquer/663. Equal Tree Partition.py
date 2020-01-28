Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:

Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:

The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000


code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #stack用来存从底到顶的路径和
        self.stack = []
        
        self.get_sum(root)
        
        #stack顶为总和，取出来作为一半的判定条件，不要栈顶点是因为顶点不能分 
        sum = self.stack.pop()
        
        #如果总和为奇数，则必定不能分 
        if sum % 2:
            return False
        
        #遍历栈里的每一个数
        while self.stack:
            node = self.stack.pop()
            #如果有节点为总值的一半，则这棵树可以均分
            if node == sum / 2:
                return True
        
        return False
    
    #分治法求和
    def get_sum(self, root):
        if not root:
            return 0
        
        left = self.get_sum(root.left)
        right = self.get_sum(root.right)
        
        sum = left + right + root.val
        
        self.stack.append(sum)
        
        return sum

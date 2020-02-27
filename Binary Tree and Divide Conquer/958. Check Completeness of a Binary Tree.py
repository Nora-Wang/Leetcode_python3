Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.


BFS遍历所有node,用miss_flag来代表前面是否有node为Null

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = collections.deque([root])
        miss_flag = False
        
        while queue:
            node = queue.popleft()
            if not node:
                miss_flag = True
                continue
            
            #这里的意思是,当前node存在,但在当前node之前有node缺失,证明其不是complete binary tree
            if miss_flag:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
        
        return True

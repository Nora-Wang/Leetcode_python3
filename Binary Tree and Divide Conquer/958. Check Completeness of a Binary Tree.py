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

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = collections.deque([root])
        
        flag = False
        
        while queue:
            node = queue.popleft()
            
            #只要出现not node的情况,都标记为flag = True
            #这里注意一定要直接标记为True,而不能用flag = not flag
            #因为存在一种情况, eg: [1,2,3,5,null,null,8]. 即两个None连续,则会使得flag回到False
            if not node:
                flag = True
                continue
                
            if flag:
                return False
            
            queue.append(node.left)
            queue.append(node.right)

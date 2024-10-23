Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104



Analysis:
1. get the sum of the depth level nodes - level_sum
2. when traverse the tree, get cur_sum=node.left.val+node.right.val, then use level_sum-cur_sum to get cousins_sum
Edge case: for the root, it's always 0, and because the traverse will start from root.left and root.right, need to set root's cousin separately.
Time O(n), Space O(h)

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        level_sum = []
        while queue:
            temp = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                temp += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sum.append(temp)
        
        root.val = 0
        queue = collections.deque([root])
        index = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum = 0
                
                if node.left:
                    cur_sum += node.left.val
                if node.right:
                    cur_sum += node.right.val
                
                if node.left:
                    node.left.val = level_sum[index] - cur_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = level_sum[index] - cur_sum
                    queue.append(node.right)
            index += 1
        
        return root
            
# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs([root])
        
        root.val = 0
        return root
    
    def dfs(self, level):
        if not len(level):
            return
        
        level_sum = 0
        for node in level:
            if not node:
                continue
            if node.left:
                level_sum += node.left.val
            if node.right:
                level_sum += node.right.val
        
        next_level = []
        for node in level:
            cur_sum = 0
            if node.left:
                cur_sum += node.left.val
            if node.right:
                cur_sum += node.right.val
                
            if node.left:
                node.left.val = level_sum - cur_sum
                next_level.append(node.left)
            if node.right:
                node.right.val = level_sum - cur_sum
                next_level.append(node.right)
        
        self.dfs(next_level)
        
        return
            
            

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # DFS create graph
        graph = collections.defaultdict(list)
        self.create_graph(root, graph)
        
        # BFS distance traverse
        queue = collections.deque([target])
        visited = set([target])
        res = []
        while queue and K >= 0:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            K -= 1
            if K == -1:
                res = list(level)
        
        return res
    
    def create_graph(self, root, graph):
        if not root:
            return
        
        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
        if root.right:
            graph[root].append(root.right)
            graph[root.right].append(root)
        
        self.create_graph(root.left, graph)
        self.create_graph(root.right, graph)

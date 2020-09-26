Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.


#07/15/2020
# BFS
# n = number of nodes, k = width of the tree
# time: worse case O(nlogn), average O(nlog(n / k))
# space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        hash_record = collections.defaultdict(list)
        
        self.traverse(root, hash_record)
        
        min_index = min(hash_record.keys())
        
        res = [None] * len(hash_record)
        for key, value in hash_record.items():
            value.sort(key=lambda x:(x[1], x[0]))
            res[key - min_index] = [x[0] for x in value]
        
        return res
    
    def traverse(self, root, hash_record):
        queue = collections.deque([(root, 0)])
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node, index = queue.popleft()
                hash_record[index].append([node.val, level])

                if node.left:
                    queue.append((node.left, index - 1))
                if node.right:
                    queue.append((node.right, index + 1))
            
            level += 1
        
        return
        
        
# DFS
# n = number of nodes, k = width of the tree
# time: worse case O(nlogn), average O(nlog(n / k))
# space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # {index: (level, value)}
        hash_record = collections.defaultdict(list)
        self.traverse(root, hash_record, 0, 0)
        
        min_index = min(hash_record.keys())
        
        res = [None] * len(hash_record)
        for index, v in hash_record.items():
            res[index - min_index] = [v[1] for v in sorted(v)]
        
        return res
    
    def traverse(self, root, hash_record, level, index):
        if not root:
            return
        
        hash_record[index].append((level, root.val))
        
        self.traverse(root.left, hash_record, level + 1, index - 1)
        self.traverse(root.right, hash_record, level + 1, index + 1)





参考leetcode 314
主要的区别就是这道题要求当index和level都相同时，按照node.val的大小进行排序，而314则是根据从左到右的顺序 #因为level traverse直接满足这一条件，因此不需要另外sort
BFS和DFS都需要另外加入level，因为先对hash_table按照key=index进行排序，然后对value=(level, node.val)进行排序
#注意这里直接写成value.sort()即可。先按level再按node.val进行排序


1. BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, 0)])
        hash_table = collections.defaultdict(list)
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node, index = queue.popleft()

                hash_table[index].append((level, node.val))

                if node.left:
                    queue.append((node.left, index - 1))
                if node.right:
                    queue.append((node.right, index + 1))
            
            level += 1
        
        sorted_hash = sorted(hash_table.items(), key=lambda x:x[0])
        
        res = []
        for _, value in sorted_hash:
            value.sort()
            temp = [v[1] for v in value]
            res.append(temp)
        
        return res
        
        
        
        
2. DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        hash_table = collections.defaultdict(list)
        
        self.helper(root, 0, 0, hash_table)
        
        sorted_hash = sorted(hash_table.items(), key=lambda x:x[0])
        
        res = []
        for _, value in sorted_hash:
            value.sort()
            res.append([v[1] for v in value])
        
        return res
    
    def helper(self, root, index, level, hash_table):
        if not root:
            return
        
        hash_table[index].append((level, root.val))
        self.helper(root.left, index - 1, level + 1, hash_table)
        self.helper(root.right, index + 1, level + 1, hash_table)

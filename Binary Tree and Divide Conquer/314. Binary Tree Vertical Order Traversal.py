Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

注意一定要用BFS来遍历树：example 3中，node 8 要比node 2先被加入list
#use BFS to traverse the tree!!
#utilize left node -> index - 1, right node -> index + 1
#time: O(n), space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        record = collections.defaultdict(list)
        
        self.traverse(root, record)
        
        res = [0] * len(record)
        min_index = min(record.keys())
        
        for key, value in record.items():
            res[key - min_index] = value
        
        return res
    
    def traverse(self, root, record):
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, index = queue.popleft()
            record[index].append(node.val)
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))







用index, left -> index - 1, right -> index + 1

难点:如何存储数据
1. BFS
使用queue,将node和index同时放入queue中,然后用hashtable value为list存储所有结果,最后sort一下即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, 0)])
        hash_table = collections.defaultdict(list)
        
        while queue:
            node, index = queue.popleft()
            
            hash_table[index].append(node.val)
            
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))
        
        sorted_hash = sorted(hash_table.items(), key=lambda x:x[0])
        
        res = [value for _, value in sorted_hash]
        
        return res
        
        

      
      
2. DFS
#DFS有个注意点：
#hash表建立的时候不仅仅需要算index，还需要记录当前node的level。
#因为根左右的顺序进行DFS会把左边的node先遍历完，这样会使得左侧level更大的node会比同等index的右侧node先append进temp。这不符合题目要求。
#因此还需要对value中的值按照level单独进行排序。eg：[3,9,8,4,0,1,7,null,null,null,2,5]
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        hash_table = collections.defaultdict(list)
        
        self.helper(root, 0, 0, hash_table)
        
        #sort the hash_table by index
        #[(index, (value, level)]
        hash_table = sorted(hash_table.items(), key=lambda x:x[0])
        
        res = []
        for _, value in hash_table:
            #sort value by level
            value.sort(key=lambda x:x[1])
            temp = [v[0] for v in value]
            res.append(temp)
        
        return res
    
    def helper(self, root, index, level, hash_table):
        if not root:
            return
        
        hash_table[index].append((root.val, level))
        self.helper(root.left, index - 1, level + 1, hash_table)
        self.helper(root.right, index + 1, level + 1, hash_table)

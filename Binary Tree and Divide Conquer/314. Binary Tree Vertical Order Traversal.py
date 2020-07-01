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


用index, left -> index - 1, right -> index + 1

难点:如何存储数据
1. BFS
使用queue,将node和index同时放入queue中,然后用hashtable value为list存储所有结果,最后sort一下即可

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, 0)])
        
        res_hash = collections.defaultdict(list)
        
        while queue:
            root, index = queue.popleft()
            res_hash[index].append(root.val)
            
            if root.left:
                queue.append((root.left, index - 1))
            if root.right:
                queue.append((root.right, index + 1))
        
        return [res_hash[i] for i in sorted(res_hash.keys())]

      
      
2. DFS
#DFS有个注意点：需要区分level，否则由于根左右的顺序，可能level大的node会先被append进temp
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

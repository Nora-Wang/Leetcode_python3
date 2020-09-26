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


用hash表来存储数据,将左子树记为x-1,右子树记为x+1
x为key,node.val记在hash的list类型的value中,这样在后续直接将hash表按照key值排序,依次输出对应的value即可

# BFS
# time: O(nlogn), space: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        #用这个function创建一个value为list的dict,很快
        record = collections.defaultdict(list)
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, index = queue.popleft()
            record[index].append(node.val)
            
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))
         
        #将record按照key值排序,将每个key对应的list_value输出
        return [record[i] for i in sorted(record)]
        
# leetcode 987 method     
# 这题BFS只需要index即可，因为这里的比较是
# 1. from top to bottom
# 2. If two nodes are in the same row and column, the order should be from left to right.

# DFS则需要加入level，因为需要满足第一个条件from top to bottom


# BFS + hashtable
# time: O(nlog(n / k)), space: O(n)
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


# DFS + hashtable
# time: O(nlog(n / k)), space: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # {index:(level, value)}
        record = collections.defaultdict(list)
        
        self.DFS(root, record, 0, 0)
        
        res = [None] * len(record)
        min_index = min(record.keys())
        
        for key, value in record.items():
            value.sort(key=lambda v:v[0])
            res[key - min_index] = [v[1] for v in value]
        
        return res
    
    def DFS(self, root, record, level, index):
        if not root:
            return
        
        record[index].append((level, root.val))
        
        self.DFS(root.left, record, level + 1, index - 1)
        self.DFS(root.right, record, level + 1, index + 1)

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000


code:
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
brute force
utilize left/right to iterate to find the next node
time: O(n^2), space: O(n)

optimize:
#level traverse by BFS
record all nodes by level to level, use a for loop to add the next node
queue(BFS), prev(record the previous node)
if change level, prev = None. if prev = None, prev = curt root; if prev exist, prev.next = curt root

time: O(n), space: O(n)
edge case: if not root, return None
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        inital = root
        queue = collections.deque([root])
        
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if prev:
                    prev.next = node
                
                prev = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

         
         
         
# 以每层最左侧的node为level_head，用prev = level_head代表当前层的head
# 然后将prev的左孩子与右孩子连起来，若prev有next，则需要将prev的右孩子与prev.next的左孩子连起来；使用while循环将当前prev层的所有node的子孩子都连起来
# 再将level_head挪到level_head.left
'''
follow up:
use head node to represent every level in the tree. 
complete the problem level by level, so for curt level(level 2), the prev level(level 1)'s nodes have .next node

head, head.next (level 1)
if head.left exist -> head.left.next = head.right (level 2)
if head.next exist, which means head is not the lase node of level 1, so the right child of head and the left child of 
head.next should be connected -> head.right.next = head.next.left (level 1 + level 2)

time: O(n), space: O(1)
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        level_head = root
        
        #use level 1's next node to deal with level 2's nodes. level_head.left is to ensuranece level 2's existine
        while level_head.left:
            #most left node in the level 1
            prev = level_head
            
            #traverse all the nodes in the level 1
            while prev:
                #connect curt node's left and right child in level 2
                prev.left.next = prev.right
                #if there still have node in level 1, connect them in level 2
                if prev.next:
                    prev.right.next = prev.next.left
                    
                prev = prev.next
            
            level_head = level_head.left
        
        return root

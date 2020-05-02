Given a binary tree

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



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100


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
#BFS level traverse
utinize BFS to traverse the tree level by level, use prev to record the previous node
helper(root, prev)
if change to another level, prev = None. 
if prev not exist, prev = root
if pre exist, prev.next = curt root

base case: if not root, return

time: O(n), space: O(n)
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
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
        
        




follow up
'''
referral:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        record = root 
        
        #loop all levels
        while root:
            curt = temp = Node(None)
            #loop all nodes in curt level
            #connect all nodes in a linkedlist
            while root:
                curt.next = root.left
                if curt.next:
                    curt = curt.next
                curt.next = root.right
                if curt.next:
                    curt = curt.next

                root = root.next
            
            #there is a littel tricky, because temp means the dummy, and for the 102 row code -> temp = root.left 
            #-> the first node in the next level
            root = temp.next
            
        return record

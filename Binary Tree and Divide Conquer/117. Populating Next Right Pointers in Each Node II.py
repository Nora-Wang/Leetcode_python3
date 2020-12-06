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

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 思路：对于每一层从最左侧的node开始
# 对于第一层来说使用curt来代表当前层的node
# 利用来将curt的下一层所有的node连到一起：prev = sub_head = Node(None), prev.next等于curt的left/right，若prev.next存在则挪动prev，否则使用覆盖的原理寻找下一个node
# curt = sub_head
# 这题最tricky的点是利用prev.next
# time: O(n), space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        level_head = root
        
        # 这里的while循环条件与116不同
        # 116是因为整个思路就是用up_level链接sub_level，因此只要保证sub_level一定存在，就可以继续循环
        # 而这里是因为由于不能保证sub_level_head的子节点是否存在，只能一行一行的都判断一遍
        # case：[3,9,20,null,null,15,7]，当level_head指向9时，由于9没有左右子节点，若根据level_head是否有字节点作为判断依据则无法进行下一步循环
        while level_head:
            curt = level_head
            prev = sub_head = Node(None)
            
            while curt:
                prev.next = curt.left
                if prev.next:
                    prev = prev.next
                    
                prev.next = curt.right
                if prev.next:
                    prev = prev.next
                
                curt = curt.next
            
            level_head = sub_head.next
        
        return root

         
         
         
# 冗长版
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# time: O(n), space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        head = root
        
        while head:
            # find the valid head with sub_head
            sub_head = None
            while head and sub_head == None:
                if head.left:
                    sub_head = head.left
                elif head.right:
                    sub_head = head.right
                else:
                    head = head.next
            
            # utilize head level to connect sub_head level
            curt = head
            previous = None
            while curt:
                if curt.left:
                    if previous:
                        previous.next = curt.left
                    previous = curt.left
                
                if curt.right:
                    if previous:
                        previous.next = curt.right
                    previous = curt.right
                
                curt = curt.next
            
            head = sub_head
        
        return root
            
            

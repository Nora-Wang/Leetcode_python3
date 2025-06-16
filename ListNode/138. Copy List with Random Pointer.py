A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 2025/6/16
# time: O(n), space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        record = {}
    
        # copy node to map
        old = head
        while old:
            record[old] = Node(old.val)
            old = old.next
        
        # copy random
        old = head
        while old:
            if old.next:
                record[old].next = record[old.next]
            if old.random:
                record[old].random = record[old.random]
            
            old = old.next
        
        return record[head]


    

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# time: O(n), space: O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        dummy = new_curt = Node(0)
        # {old_node:new_node}
        record = {}
        
        # copy val ans store in record
        old_curt = head
        while old_curt:
            new_curt.next = Node(old_curt.val)
            record[old_curt] = new_curt.next
            
            new_curt = new_curt.next
            old_curt = old_curt.next
        
        # copy random
        old_curt = head
        new_curt = dummy.next
        while old_curt:
            if old_curt.random:
                new_curt.random = record[old_curt.random]
            
            new_curt = new_curt.next
            old_curt = old_curt.next
        
        return dummy.next
            


# time: O(n), space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # copy val
        curt = head
        while curt:
            new_node = Node(curt.val)
            new_node.next = curt.next
            curt.next = new_node
            
            curt = curt.next.next
        
        # copy random
        curt = head
        while curt:
            new_curt = curt.next
            if curt.random:
                new_curt.random = curt.random.next
            
            curt = curt.next.next
        
        # get new_head
        dummy = new_head = Node(0)
        curt = head
        while curt:
            new_head.next = curt.next
            
            curt = curt.next.next
            new_head = new_head.next
        
        return dummy.next

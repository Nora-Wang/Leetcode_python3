题目:
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

思路：
一个快指针一个慢指针，如果路径上有环，快慢指针一定会相遇

快慢指针模板:
slow = fast = head
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next


code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
     
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 这个一定要放在后面，因为一开始setting的时候slow = fast = head，放在前面的话，anyway都会return True
            if fast == slow:
                return True
           
        return False
       

# Hashset
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        record = set()
        
        while head:
            if head in record:
                return True
            
            record.add(head)
            head = head.next
        
        return False

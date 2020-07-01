Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5



#06/30/2020
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 1. end case
        if not head or not head.next:
            return head
        
        # 2. divide 
        prev, slow, fast = ListNode(None), head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        fast = slow
        slow = head
        
        # 3. sorting
        slow = self.sortList(slow)
        fast = self.sortList(fast)
        
        # 4. comquer
        #merge two sorted linked list
        dummy = ListNode(None)
        curt = dummy
        while slow and fast:
            if slow.val < fast.val:
                curt.next = slow
                slow = slow.next
            else:
                curt.next = fast
                fast = fast.next
            curt = curt.next
        
        curt.next = slow if slow else fast
        
        return dummy.next

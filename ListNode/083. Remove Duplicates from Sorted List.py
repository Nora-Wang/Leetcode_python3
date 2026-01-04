题目：

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


# 01/04/2026
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        dummy = ListNode()
        dummy.next = head

        cur, head = dummy.next, head.next

        while head:
            while head and head.val == cur.val:
                head = head.next

            cur.next = head
            cur = cur.next

            if head:
                head = head.next
        
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head


思路：
设置一个ListNode curt = head的头指针
若curt.val = curt.next.val则将curt的指针指向curt.next.next，即将curt.next这个node从head中删掉

'''
易错case：
1. if curt.val != prev.val:
        prev.next = curt
        prev = prev.next
            
   curt = curt.next
   出现case: [1,1,2,3,3] -> [1,2,3,3]
2. 若要使用dummy，需要注意dummy node的val的设置;因为head.val可能会任意值(0, -1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(n), space: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        curt = head
        
        while curt.next:
            if curt.val == curt.next.val:
                curt.next = curt.next.next
            else:
                curt = curt.next
        
        return head
        
        
        
        

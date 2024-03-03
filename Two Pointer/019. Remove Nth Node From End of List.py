题目：
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.


思路：
fast与slow之间相隔n个数
注意：例[1,2,3,4,5] n=2
最后fast = 5时，slow=2；即被删除的数为slow.next = 3；用slow.next = slow.next.next将node删除

注意：slow.next = slow.next.next
此处成立是因为n的取值>=1（Given n will always be valid.），且head不为空




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(None)
        dummy.next = head
        
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next


# 遍历两遍
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        count_head = head
        while count_head:
            count += 1
            count_head = count_head.next
        
        cur = dummy = ListNode(None)
        dummy.next = head
        step = 1
        
        for _ in range(count - n):
            cur = cur.next
        
        cur.next = cur.next.next
        
        return dummy.next
            
            

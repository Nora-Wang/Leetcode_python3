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
        dummy = ListNode(None)
        dummy.next = head
        #fast和slow都由空指针开始，避免[1],n=1
        slow = fast = dummy
        while(n and fast):
            fast = fast.next
            n -= 1
        while(fast.next and slow.next):
            slow = slow.next
            fast = fast.next
        #Given n will always be valid.
        slow.next = slow.next.next
        return dummy.next

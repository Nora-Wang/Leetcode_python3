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
        #fast和slow都由空指针开始，且相距n个node
        slow = fast = dummy
  ##第二次做的注意点：fast.next
        while(n and fast.next):
            fast = fast.next
            n -= 1
        while(fast.next):
            slow = slow.next
            fast = fast.next
  ##第二次写的时候没有加上前面的fast.next,用的解决方案为
        # if not (temp):
        #     return head.next
        
        #Given n will always be valid.
        slow.next = slow.next.next
        return dummy.next
    
    
    第二次做，想到的办法是n = count - n，但这样的时间复杂度高

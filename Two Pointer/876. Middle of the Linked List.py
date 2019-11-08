题目：
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.


思路：
寻找指针链表中点，快慢指针，快指针每次走两步，慢指针每次走一步，快指针走到链表结尾时，慢指针在中间

难点：while循环的判断条件   while(fast and fast.next)
可以举例子：
奇数个node循环结果为fast在最后一个node处，因此fast
偶数个node循环结果为fast在最后一个node.next（If there are two middle nodes, return the second middle node）因此fast.next




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow

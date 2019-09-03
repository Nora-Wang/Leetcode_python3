题目：

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL



思路：
翻转m和n之间的部分，分为三个步骤：
1. 用while(m - 1)找到m-1和m的点，设为prev和curt，记录start_prev = prev；start = curt；

   此时start_prev表示反转链表的前一个node，start表示反转链表的最后一个node
   
2. 用k = n - m；while(k)将m~n反转；

   此时prev代表反转链表的第一个node，curt代表整个反转链表的下一个node
   
3. 把start_prev.next = prev;把start.next = curt




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        k = n - m
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curt = head
        #为记录反转链表的前一个node，需循环m-1次，使得start_prev = prev
        while(m - 1):
            prev = prev.next
            curt = curt.next
            m -= 1
        start_prev = prev
        start = curt
        prev = curt
        curt = curt.next
        while(k):
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
            k -= 1
        start_prev.next = prev
        start.next = curt
        return dummy.next
        
        
        

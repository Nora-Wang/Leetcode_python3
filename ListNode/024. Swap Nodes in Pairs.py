题目：
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.



思路：
              1       ->        2          ->         3
prev, curt = prev.next, temp = curt.next

使prev指向2，temp = 2指向1，curt = 1指向3；这里temp和curt的顺序需要换一下，因为curt指向3的方法为curt = temp.next，在temp更改之前得完成

难点：
while循环的条件
dummy.next = head可满足特殊情况
循环结束的情况（仅剩一个node:temp == None和无node:curt == None时，都标志着swap结束）





code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        #考虑[]和[1]的情况，若不用while循环，return dummy.next可直接返回head
        dummy.next = head
        prev = dummy
        
        while(prev.next and prev.next.next):
            curt = prev.next
            #共偶数个node：1->2->3->4.循环结束，prev指向最后一个node；即整个链表swap结束
            if not (curt):
                break
            temp = curt.next
            #共奇数个node：1->2->3->4->5.循环结束，prev指向倒数第二个node；此时仅剩一个node，即整个链表swap结束
            if not (temp):
                break
            prev.next = temp
            curt.next = temp.next
            temp.next = curt
            prev = curt
        return dummy.next

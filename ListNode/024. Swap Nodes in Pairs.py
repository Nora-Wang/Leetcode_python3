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
#####提前定义了curt，使得在while循环中不用单独判定curt和temp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(None)
        dummy.next = curt = head
        
        while curt and curt.next:
            #定义好temp,curt,prev的位置
            temp = curt.next
            
            #开始swap:1->4, 3->5, 4->3
            prev.next = temp
            curt.next = temp.next
            temp.next = curt
            
            #调整一下当前prev和curt的位置
            prev = curt
            curt = curt.next
        
        return dummy.next
            
            
            

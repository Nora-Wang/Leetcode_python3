题目：
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


思路：
以l1为标准，若l2<l1将l2插入
有两点很奇怪：
1.curt.next.next = None
2.if(l1 == None)不能改为if(l1)




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curt = dummy
        while(l1 and l2):
            if(l1.val > l2.val):
                curt.next = l2
                l2 = l2.next
            else:
                curt.next = l1
                l1 = l1.next
                
            #若无下一语句，时间为20ms；若有，时间为16ms
            curt.next.next = None
            curt = curt.next
            
        #若为if(l1)，则结果出错
        if(l1 == None):
            curt.next = l2
        elif(l2 == None):
            curt.next = l1
        
        return dummy.next

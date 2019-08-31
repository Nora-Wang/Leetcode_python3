题目：

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

思路：
设置一个ListNode curt = head的头指针
若curt.val = curt.next.val则将curt的指针指向curt.next.next，即将curt.next这个node从head中删掉




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return None
        curt = head
        
        while(curt.next != None):
            if(curt.val != curt.next.val):
                curt = curt.next
            else:
                curt.next = curt.next.next
            
        return head
        
        
        
        

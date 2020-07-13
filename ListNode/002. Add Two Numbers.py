You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

    
    
#time: O(n1 + n2), space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        curt = 0
        
        while l1 or l2 or curt:
            if l1:
                curt += l1.val
                l1 = l1.next
            if l2:
                curt += l2.val
                l2 = l2.next
                
            head.next = ListNode(curt % 10)
            head = head.next
            
            curt //= 10
        
        return dummy.next
    
    
    


code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = dummy = ListNode(0)
        
        carry = 0
        
        #这里一定要加一个carry != 0,因为最后一位可能会存在进位
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            tail.next = ListNode(carry % 10)
            carry = carry // 10

            tail = tail.next
        
        return dummy.next
        
        

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1_list, num2_list = [], []
        
        point_l1 = l1
        point_l2 = l2
        
        #先建立一个空节点，把指针指向这里 
        dummy = ListNode(None)
        tail = dummy
        #设置累加的值
        carry = 0
        
        #注意carry有值时一定要建立，可能需要进位
        while l1 or l2 or carry:
            num = 0
            #如果链表1有值，把1的值加到num上，更新l1 
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
                
            num += carry
            
            #当前节点的值digit为num % 10，只要个位数
            #carry只需要留下余数
            digit, carry = num % 10, num // 10
        
            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy.next

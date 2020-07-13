You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

    
    
#07/13/2020    
Brute Force: 先转换为数字,相加后一个一个的放入dummy
#time: O(max(n1, n2)), space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        res = num1 + num2
        #corner case: res = 0 -> 后续将没有node
        if not res:
            return ListNode()
        
        prev = None
        
        while res:
            node = ListNode(res % 10)
            node.next = prev
            prev = node
            
            res //= 10
        
        return node



Optimize Solution 1: reverse linked list
#time: O(n1 + n2), space: O(max(n1, n2))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        dummy = head = ListNode()
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
        
        return self.reverse(dummy.next)
    
    def reverse(self, head):
        tail = None
        
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        
        return tail
            
        
Optimize Solution 2: 利用stack
#time: O(max(n1, n2)), space: O(max(n1, n2))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        curt = 0
        prev = None
        while stack1 or stack2 or curt:
            if stack1:
                curt += stack1.pop()
            if stack2:
                curt += stack2.pop()
                
            node = ListNode(curt % 10)
            node.next = prev
            prev = node
            
            curt //= 10
        
        return prev
            
    
    
    
    
    
    
    
    
    

先转换为数字,相加后,转换为str,然后一个一个的放入dummy

code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(None)
        
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        res = num1 + num2
        str_res = str(res)
        for num in str_res:
            tail.next = ListNode(int(num))
            tail = tail.next
        
        return dummy.next
        

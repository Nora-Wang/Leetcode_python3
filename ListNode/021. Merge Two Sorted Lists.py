题目：
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

# Version: recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    
    
# Version: Iteration    
#06/29/2020
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curt = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curt.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curt.next = ListNode(l2.val)
                l2 = l2.next
            
            curt = curt.next
        
        if l1:
            curt.next = l1
        if l2:
            curt.next = l2
        
        return dummy.next
    
    
    
    
    
    
    
    

思路：
以l1为标准，若l2<l1将l2插入
有一点很奇怪：curt.next.next = None
若有这一句，时间为20ms；若有，时间为12ms。即这句话节省了很多时间
猜测原因：如果不赋值为none，那每次复制的时候都是l.next，即每次都把l1或者l2的剩下的值给赋值一遍


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
   #####第二次做画蛇添足的判断了一下l1和l2，时间复杂度变大
        # if not (l1):
        #     return l2
        # if not (l2):
        #     return l1
        dummy = ListNode(None)
        curt = dummy
        while(l1 and l2):
            if(l1.val > l2.val):
                curt.next = l2
                l2 = l2.next
            else:
                curt.next = l1
                l1 = l1.next
    #####第二次做还是没写这句话。。。。。
            #若无下一句，时间为20ms；若有，时间为12ms
            curt.next.next = None
            curt = curt.next
            

        if(l1):
            curt.next = l1
        elif(l2):
            curt.next = l2
        
        return dummy.next

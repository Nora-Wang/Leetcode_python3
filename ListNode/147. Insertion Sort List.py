Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5


 
#06/30/2020
#time: O(n^2), space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #corner case
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        #curt means curt compare node. the insert node will be inserted between curt and curt.next
        curt = dummy
        
        while head:
            #剪枝：若当前要被insert的node,head.val,比curt小,则回到dummy进行比较;若>=,则直接从当前curt继续比较即可
            if head.val < curt.val:
                curt = dummy
            
            #这里要保证curt.next的存在,因为如果curt.next不存在,则没有挪动的必要了,直接将node加到curt.next即可
            while curt.next and head.val > curt.next.val:
                curt = curt.next
            
            #需要提前记录一下curt.next(也可以写出下面的代码,但是运行时间会加长)
            #curt.next = ListNode(head.val, curt.next)
            temp = curt.next
            curt.next = ListNode(head.val, temp)
            
            head = head.next
        
        return dummy.next
        
        
 
 
 
 
 
 
 
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        
        while head:
            tail = dummy
            
            #注意这里是对tail.next.val与head.val做比较
            while tail.next and head.val > tail.next.val:
                tail = tail.next
            
            #temp=3, tail=2, tail.next=4: 先将3->4, 然后2->3
            temp = ListNode(head.val)
            temp.next = tail.next
            tail.next = temp
            
            head = head.next
        
        return dummy.next

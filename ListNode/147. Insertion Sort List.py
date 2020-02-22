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

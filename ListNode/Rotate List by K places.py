Given a list, rotate the list to the right by k places, where k is non-negative.

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Input: 1->2->3->4->5->NULL, k = 12
Output: 4->5->1->2->3->NULL



Solution:
#个人认为空间复杂度除开output，中间都是constant space
#time: O(n), space: O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def RotateKPlace(self, head, k):
        #get the length of head
        length = 0
        curt = dummy = LinkedList(None)
        dummy.next = head
        while curt:
            length += 1
            curt = curt.next

        #get the real k
        k = length - k % length - 1

        #find the rotate place
        curt = head
        while k:
            k -= 1
            tail = curt.next

        #if the rotate place is the end of the linked list -> return directly
        if not curt.next:
            return head

        #record the right part
        new_head = curt.next
        dummy = LinkedList(None)
        dummy.next = new_head

        #connect the left part
        while new_head.next:
            new_head = new_head.next
        curt.next = None
        new_head.next = head

        return dummy.next




solution = Solution()

nums1 = [1, 2, 3, 4]
dummy = LinkedList(None)
head = dummy
for num in nums1:
    head.next = LinkedList(num)
    head = head.next

result1 = solution.RotateKPlace(dummy.next, 12)


while result1:
    print(result1.value, '->', end=' ')
    result1 = result1.next
print(result1)

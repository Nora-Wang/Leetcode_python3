Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# odd:
1, 2, 3 -> compare previous and slow.next
p, s, f
# even:
1, 2, 3, 4 -> compare previous and slow
   p, s,   f

# time: O(n), space: O(1) (reverse half linkedlist in-place)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        prev = ListNode()
        slow, fast = head, head
        while fast and fast.next:
            # 先写fast，因为后续reverse的时候会将原linkedlist进行更改，这会影响fast的结果
            fast = fast.next.next
            # reverse previous linkedlist
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # 若为odd，则move slow
        if fast:
            slow = slow.next  
        
        # varify palindrome
        left, right = prev, slow
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
            
        
        

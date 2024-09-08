Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50



# Utilize quotient and remainder to generate the List
# quotient, remainder = len(head) // k, len(head) % k
# For the first remainder ListNodes in result, they should have length of quotient+1 ListNode, and the k-remainder ListNodes should have quotient ListNode
# Time O(max(len(head), k)), Space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        quotient, remainder = length // k, length % k
        
        result = []
        cur = head
        while cur:
            dummy = ListNode()
            dummy.next = cur
            
            count = 1
            while cur and count < quotient:
                cur = cur.next
                count += 1

            # count < quotient + 1: Edge Case, such as head = [1,2,3], k = 5, cur is 1, and remainder is 3, it's incorrect to go to cur.next
            if remainder > 0 and count < quotient + 1 and cur:
                cur = cur.next
                remainder -= 1
            
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
                result.append(dummy.next)

        # Edge case, such as head = [1,2,3], k = 5, k is larger than lenght of head
        for _ in range(len(result), k):
            result.append(None)
        
        return result


# 写法上的optimize
# https://leetcode.com/problems/split-linked-list-in-parts/discuss/5752989/Beats-100-Explained-with-Video-C%2B%2BJavaPython-O(n)-Time-O(k)-Space-Explained-in-Detail
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        quotient, remainder = length // k, length % k
        
        cur = head
        for i in range(k):
            result[i] = cur
            current_size = quotient + 1 if remainder > 0 else quotient
            remainder -= 1
            
            for _ in range(current_size - 1):
                if cur:
                    cur = cur.next
            
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
        
        return result
            
            

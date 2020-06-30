Reverse pairs of elements in a singly-linked list.

Examples
	•	L = null, after reverse is null
	•	L = 1 -> null, after reverse is 1 -> null
	•	L = 1 -> 2 -> null, after reverse is 2 -> 1 -> null
	•	L = 1 -> 2 -> 3 -> null, after reverse is 2 -> 1 -> 3 -> null





Solution:
#time: O(n), space: O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def ReversePairs(self, head):
        dummy = LinkedList(None)
        dummy.next = head
        #指向上一组的尾
        tail = dummy
        #指向当前组的头
        curt = tail.next

        #保证能够两个两个一组的翻转
        while curt and curt.next:
            prev = LinkedList(None)
            for _ in range(2):
                temp = curt.next
                curt.next = prev
                prev = curt
                curt = temp

            tail.next = prev
            tail = prev.next

        #若最后一组还剩一个node时,则链接到倒数第二组的尾
        tail.next = curt

        return dummy.next




solution = Solution()

nums1 = [1, 2, 3, 4]
dummy = LinkedList(None)
head = dummy
for num in nums1:
    head.next = LinkedList(num)
    head = head.next

result1 = solution.ReversePairs(dummy.next)


while result1:
    print(result1.value, '->', end=' ')
    result1 = result1.next
print(result1)

Given a linked list and a sorted array of integers as the indices in the list. Delete all the nodes at the indices in the original list.

Examples
1 -> 2 -> 3 -> 4 -> NULL, indices = {0, 3, 5}, after deletion the list is 2 -> 3 -> NULL.

Assumptions
	•	the given indices array is not null and it is guaranteed to contain non-negative integers sorted in ascending order.
  
  

Solution:
#time: O(n), space: O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def DeleteIndex(self, head, indices):
        dummy = LinkedList(None)
        dummy.next = head
        #prev.next才是要删除的node
        prev = dummy

        #此时index指向prev的indice,因此为-1
        index = -1
        while prev and prev.next:
            #先加一,即当前index指向prev.next -> 判断prev.next是否为要删除的node
            index += 1
            
            #可能会出现连续node都被删除的情况,因此使用一个while循环.保证prev会被挪到一个不会被删除的node上
            while index in indices and prev.next:
                prev.next = prev.next.next
                index += 1

            prev = prev.next

        return dummy.next



solution = Solution()

nums1 = [1, 2, 3, 4]
dummy = LinkedList(None)
head = dummy
for num in nums1:
    head.next = LinkedList(num)
    head = head.next

indices = {0, 2, 5}

result1 = solution.DeleteIndex(dummy.next, indices)


while result1:
    print(result1.value, '->', end=' ')
    result1 = result1.next
print(result1)

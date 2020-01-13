Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


code:
#Version 1 priority queue / heap
这道题用heap:lista中存在k个list,首先将这k个list的head放入heap,然后pop,因为用的heapq,即最小堆,其pop的值一定是当前k个数的最小值;
            此时这个最小值所在的list的head则向后挪一位,同时将该point又push进heap中,然后再重新pop最小值
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #corner case:
        #lists = None, return None
        #lists = [], return []
        if not lists:
            return None
        
        heap = []
        #将所有list的head放入heap
        for head in lists:
            #这里要这样写是因为corner case:lists = [[]], return [];这样head没有val
            if head:
                heapq.heappush(heap, (head.val, head))
        
        #因为rtype: ListNode,所以新建一个dummy
        dummy = ListNode(-1)
        tail = dummy
        
        #heap就跟queue一样的用
        while heap:
            _, head = heapq.heappop(heap)
            tail.next = head
            tail = head
            #这里不能将tail后面清空,因为这里改tail就等同对head(lists中的head)做改变
            #tail.next = None

            if head.next:
                head = head.next
                heapq.heappush(heap, (head.val, head))
        
        return dummy.next

#Version 2


#Version 3

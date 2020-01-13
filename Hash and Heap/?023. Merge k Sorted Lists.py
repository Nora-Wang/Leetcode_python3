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
这个方法的时间复杂度为O(nlogk),因为一共有n个点,需要循环n次来对它们排序;而每次是用具有k个points的heap中直接pop出来的,这个时间是logk
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

#Version 2 使用merge sort的原理:merge two by two自底向上的两两归并方法，最容易实现和思考 
即一共有k个list,然后将lists两两merge(若只剩一个则直接加入lists),这样无限两两merge,最后就能得到所有的lists被merge成一个linkedlist的结果
这里的时间复杂度为O(nlogk),即相当于一个有k个node的二叉树,其高度为logk(一共需要logk次的两两merge),而每次merge的points的个数最差为n
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #corner case
        if not lists:
            return None
        
        #当lists还没有被merge得只剩下一个linkedlist时,就需要继续merge
        while len(lists) > 1:
            new_lists = []
            
            #注意点:range(start, end, step),其中step默认为1,但当step!=1时,一定要记得将start补全,不然会默认将我们需要的step当作end
            for i in range(0, len(lists), 2):
                #因为后续需要用到i+1,因此需要特判,看是否在范围内
                if i + 1 < len(lists):
                    new_list = self.merge_two_list(lists[i], lists[i + 1])
                #这里else的意思即当前i为lists的最后一个list,此时不用两两merge,直接将其加入new_lists即可
                else:
                    new_list = lists[i]
                new_lists.append(new_list)

            lists = new_lists

        return lists[0]
    
    #处理的时候一定要记住,这里的数据类型为ListNode,它包含.val和.next,不要直接当作list来用
    def merge_two_list(self, list1, list2):    
        dummy = tail = ListNode(-1)
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            #tail.next = None
            
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next
                

#Version 3

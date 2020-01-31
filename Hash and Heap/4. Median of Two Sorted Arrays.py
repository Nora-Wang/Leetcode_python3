There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


基本上就是用最小堆与最大堆求中位数的模板

code:
import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.min_heap = []
        self.max_heap = []
        
        nums = nums1 + nums2
        
        for i in range(len(nums)):
            self.heap_add(nums[i])
        
        return self.get_median()
    
    def heap_add(self, num):
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if self.min_heap and self.min_heap[0] < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    
    def get_median(self):
        if not self.min_heap:
            return -self.max_heap[0]
        
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2
        
        return -self.max_heap[0]

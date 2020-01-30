Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.


code:
import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums:
            return []
        
        self.min_heap = []
        self.max_heap = []
        
        for i in range(k):
            self.heap_add(nums[i])
        
        result = []
        median = self.get_median()
        result.append(median)
        #print max_heap, min_heap, median

        for j in range(len(nums) - k):
            if -nums[j] in self.max_heap:
                self.max_heap.remove(-nums[j])
                heapq.heapify(self.max_heap)
            else:
                self.min_heap.remove(nums[j])
                heapq.heapify(self.min_heap)
                
            self.heap_add(nums[j + k])
            
            median = self.get_median()
            #print max_heap, min_heap, median
            result.append(median)
        
        return result
            
    
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
        

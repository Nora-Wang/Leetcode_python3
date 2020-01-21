Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


code:
Version 1:QuickSelect
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
            
#一定要return！！！！
        return self.quickselect(nums, 0, len(nums) - 1, k)
        
    def quickselect(self, nums, start, end, k):
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[start + (end - start) // 2]
        
        #partition
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
#此时要分3个情况分析，因为最坏情况会将nums分为三部分：[start, right], pivot, [left, end]
#k可能会存在于这三个地方
        #注意，这里的k是第k个值，而start和right是index，因此需要-1
        if start + k - 1 <= right:
#一定要return！！！！
            return self.quickselect(nums, start, right, k)
            
        if start + k - 1 >= left:
#一定要return！！！！
        #注意这里要搞清楚新k值的取值逻辑，相当于已经判断出k不可能出现在[start, right]和pivot部分，因此要将前面的部分去掉从而得到一个新的k值
            return self.quickselect(nums, left, end, k - (left - start))
        
        return pivot

    
Version 2:priority queue
    
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for item in nums:
            heapq.heappush(heap, item)
            
        while len(heap) > k:
            heapq.heappop(heap)
            
        return heap[0]
    

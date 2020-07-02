Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

#clarification
what's the relationship between k and n?
if k >= n -> return nums

************************************************************************************************************
Solution:
1. brute force: sort and get kth element -> time: O(nlogn)
2. quick select sort -> time: O(n) ~ O(n^2) depends on the pivot, space: O(1) or O(logn) ~ O(n)(recursion extra space)
3. min_heap: heapify + pop len(nums)-k+1 elements -> time: O(n) + O((n - k)logn), space: O(n)
4. max_heap: create a k length max_heap + push n-k element into the heap -> time: O(k) + O((n - k)logn), space: O(k)

************************************************************************************************************
#1. brute force
#sort the whole array directly, return the kth element
#time: O(nlogn), space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
    
#time: O(nlogn), space: O(1) or O(n)(recursion extra space)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
    
************************************************************************************************************    
#2. quick select
#time: O(n) ~ O(n^2) depends on the pivot, space: O(1) or O(logn) ~ O(n)(recursion extra space)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        return self.quick_select(nums, 0, len(nums) - 1, k)
    
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        #start ~ right, pivot, left ~ end
        #这里是直接return,相当于二分思想,将另一部分直接舍弃
        if k <= right + 1:
            return self.quick_select(nums, start, right, k)
        elif k >= left + 1:
            return self.quick_select(nums, left, end, k)
        
        return pivot
    
************************************************************************************************************    
#3. min_heap: 
#heapify + pop len(nums) - k + 1 elements
#time: O(n) + O((n - k)logn), space: O(n)
from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        
        heapq.heapify(nums)
        
        res = None
        k = len(nums) - k + 1
        while k:
            res = heapq.heappop(nums)
            k -= 1
        
        return res




code:
Version 1:QuickSelect
时间复杂度O(n)
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
#这里一定要返回一个值！！
#相当于递归的出口
        if start == end:
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
时间复杂度O(klogn)
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
    
Version 3:直接排序
时间复杂度O(nlogn)

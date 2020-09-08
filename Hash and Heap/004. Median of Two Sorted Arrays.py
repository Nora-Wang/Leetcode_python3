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

# 1. brute force: two pointer
# 使用双指针分别对两个数组遍历，比较两个指针下的元素大小，每次移动更小的指针，通过移动次数确定中位数的位置。
# time: O(n + m), space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p_1, p_2 = 0, 0
        
        # 对于odd奇数个来说，k的结果是指第k的数是median (eg: 一共7个数，k = 4)
        # 对于even偶数个来说，k的结果是指第k的数是larger_median，第k-1的数是smaller_median (eg: 一共6个数，k = 4)
        k = (len(nums1) + len(nums2)) // 2 + 1
        # 使用larger_median就是为了记录median的值，便于最后输出，不然不知道最后一步是更新的p_1还是p_2 -> 无法知道median到底是nums1[p_1] 还是 nums2[p_2]
        larger_median = None
        
        for _ in range(k):
            # 这里使用smaller_median：当偶数个数据时，需要得到两个median
            # 前面得到的k保证了最后循环结束得到的是larger_median，而整个算法是是使用two pointer一个一个数值找的，那么最后找到larger_median的上一个数据一定是smaller_median
            smaller_median = larger_median
            
            # p_1 and p_2 are both in the index range
            if p_1 < len(nums1) and p_2 < len(nums2):
                if nums1[p_1] < nums2[p_2]:
                    larger_median = nums1[p_1]
                    p_1 += 1
                else:
                    larger_median = nums2[p_2]
                    p_2 += 1
            
            # p_1 or p_2 out of index
            elif p_1 < len(nums1):
                larger_median = nums1[p_1]
                p_1 += 1
            else:
                larger_median = nums2[p_2]
                p_2 += 1
        
        # 奇数
        if (len(nums1) + len(nums2)) % 2:
            return larger_median
        # 偶数
        return (larger_median + smaller_median) / 2

# 2. binary search

# time: O(log(n + m)), space: O(1)



# 3. Heap: 基本上就是用最小堆与最大堆求中位数的模板
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

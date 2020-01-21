Find the kth smallest number in an unsorted integer array.

Example

Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:

Input: [1, 1, 1], k = 2
Output: 1
Challenge

An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


直接参考215,唯一区别就是quick select sort的结果一个为从小到大排序(461),一个为从大到小排序(215)
时间复杂度为O(n)

时间复杂度为O(nlogn)的做法:quick sort/merge sort排个序,然后直接输出即可

code:
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        if not nums or k < 1:
            return None
            
        return self.quick_select(k, nums, 0, len(nums) - 1)
        
    def quick_select(self, k, nums, start, end):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if start + k - 1 <= right:
            return self.quick_select(k, nums, start, right)
        if start + k - 1 >= left:
            return self.quick_select(k - (left - start), nums, left, end)
        
        return pivot
            
        

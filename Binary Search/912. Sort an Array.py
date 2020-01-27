Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000


code:
#Version 1: quick sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        self.quick_sort(nums, 0, len(nums) - 1)
        
        return nums
    
    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        
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
            
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)
    
    
    
#Version 2: merge sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        temp = [None] * len(nums)
        self.merge_sort(nums, 0, len(nums) - 1, temp)
        
        return nums
        
    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return 
        
        mid = (start + end) // 2
        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid + 1, end, temp)
        
        self.merge(nums, start, end, temp)
        
    def merge(self, nums, start, end, temp):
        left_index = index = start
        mid = (start + end) // 2
        right_index = mid + 1
        
        while left_index <= mid and right_index <= end:
            if nums[left_index] < nums[right_index]:
                temp[index] = nums[left_index]
                left_index += 1
            else:
                temp[index] = nums[right_index]
                right_index += 1
            index += 1
            
        while left_index <= mid:
            temp[index] = nums[left_index]
            index += 1
            left_index += 1
        
        while right_index <= end:
            temp[index] = nums[right_index]
            right_index += 1
            index += 1
            
        for i in range(start, end + 1):
            nums[i] = temp[i]

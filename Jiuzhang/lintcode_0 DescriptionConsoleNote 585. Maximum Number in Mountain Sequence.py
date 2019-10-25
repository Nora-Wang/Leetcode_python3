Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3] 
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7], 
Output: 10

二分法，和leetcode162一样


code:
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return -1
            
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= nums[mid + 1]:
                start = mid
            if nums[mid] > nums[mid + 1]:
                end = mid
        
        if nums[start] <= nums[end]:
            return nums[end]
        if nums[end] < nums[start]:
            return nums[start]
                

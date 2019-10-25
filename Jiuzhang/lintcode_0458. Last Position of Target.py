Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

注意点：当nums[mid] == target时，直接start=mid就行


code:
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
            
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1

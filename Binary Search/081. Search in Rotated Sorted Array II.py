Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?


二分+数学

code:
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return True
            
            #Tricky part
            #直接将重复部分略去
            while start < mid and nums[start] == nums[mid]:
                start += 1
            while end > mid and nums[end] == nums[mid]:
                end -= 1

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target or nums[end] == target:
            return True
        
        return False

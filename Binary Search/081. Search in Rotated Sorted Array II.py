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


# 利用while loop去重，剩余部分与leetcode 33一模一样
# time: O(logn) ~ O(n), space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            # 利用两个while循环来去重即可
            while left + 1 < right and nums[left + 1] == nums[left]:
                left += 1
            while left + 1 < right and nums[right - 1] == nums[right]:
                right -= 1
            
            mid = (left + right) // 2
            
            # end
            if nums[mid] == target:
                return True
            
            # 这里与right/left比较都可以，只要分析清楚情况即可
            # 因为重复以及相等的情况已经处理过了，只剩下了下面的情况
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
        
        if nums[left] == target or nums[right] == target:
            return True
        return False



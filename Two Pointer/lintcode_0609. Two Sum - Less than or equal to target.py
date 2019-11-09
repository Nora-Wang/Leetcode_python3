Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Example

Example 1:

Input: nums = [2, 7, 11, 15], target = 24. 
Output: 5. 
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
Example 2:

Input: nums = [1], target = 1. 
Output: 0. 



类似题目：
611. Valid Triangle Number
lintcode_0609. Two Sum - Less than or equal to target
lintcode_0443. Two Sum - Greater than target


思路直接参考611. Valid Triangle Number

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        start, end = 0, len(nums) - 1
        
        nums.sort()
        count = 0
        
        while start < end:
            if nums[start] + nums[end] <= target:
                count += end - start
                start += 1
            else:
                end -= 1
        
        return count

Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example

Example 1:

Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2



code:
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
            
        nums.sort()
        start, end = 0, len(nums) - 1
        result = set()
        
        while start < end:
            if nums[start] + nums[end] == target:
                result.add(nums[start])
            if nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
                
        return len(result)

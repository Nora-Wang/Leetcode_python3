Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Example

Example 1:

Input: [2, 7, 11, 15], target = 24
Output: 1
Explanation: 11 + 15 is the only pair.
Example 2:

Input: [1, 1, 1, 1], target = 1
Output: 6
Challenge

Do it in O(1) extra space and O(nlogn) time.




思路直接参考611. Valid Triangle Number



class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if not nums:
            return 0
            
        nums.sort()
        count = 0
        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] + nums[end] > target:
                count += end - start
                end -= 1
            else:
                start += 1
                
        return count

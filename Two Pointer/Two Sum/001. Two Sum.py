Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

由于这道题的返回值为index，并且给出的array并不是sorted的，因此只能用hash来处理

code:
使用dict，key为值，value为index
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i

            
            
# two pointer
# time: O(nlogn), space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        for i in range(len(nums)):
            nums[i] = (nums[i], i)

        nums.sort(key=lambda x:x[0])
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start][0] + nums[end][0] == target:
                return [nums[start][1], nums[end][1]]
            
            if nums[start][0] + nums[end][0] < target:
                start += 1
            else:
                end -= 1
        

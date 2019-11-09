Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

参考

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None
        
        nums.sort()
        result = None
        diff = sys.maxsize
        
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if abs(sum - target) < diff:
                    diff = abs(sum - target)
                    result = sum
                    
                if sum < target:
                    start += 1
                else:
                    end -= 1
                    
        return result

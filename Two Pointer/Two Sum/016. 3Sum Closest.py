Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

参考

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        result = 0
        record = sys.maxsize
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                value = nums[left] + nums[right] + nums[i]
                
                #特判
                if abs(target- value) < abs(target - record):
                    if value == target:
                        return value
                    record = value
                
                if value < target:
                    left += 1
                    #去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    #去重
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return record

Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the absolute value of difference between the sum of the two integers and the target.

Example

Example1

Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
Example2

Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
Challenge

Do it in O(nlogn) time complexity.

参照611. Valid Triangle Number


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        if not nums:
            return None
        
        start, end = 0, len(nums) - 1
        nums.sort()
        diff = sys.maxsize
        
        while start < end:
            if nums[start] + nums[end] == target:
                return 0
                
            if nums[start] + nums[end] < target:
                diff = min(target - (nums[end] + nums[start]) , diff)
                start += 1
            else:
                diff = min(nums[end] + nums[start] - target , diff)
                end -= 1
        
        return diff

    
    
#若要求输出这两个值
#time: O(n), space: O(1)
class Solution:
    def TwoSumClosest(self, nums, target):
        left, right = 0, len(nums) - 1
        record = [float('inf'), float('inf')]

        while left < right:
            curt = nums[left] + nums[right]
            if curt == target:
                return [nums[left], nums[right]]

            if abs(sum(record) - target) > abs(curt - target):
                record[0] = nums[left]
                record[1] = nums[right]

            if curt > target:
                right -= 1
            else:
                left += 1

        return record

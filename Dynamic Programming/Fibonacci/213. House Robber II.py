You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


    
'''
same as house robberI, but saperate to two nums
1. include first but not the last
2. include the last house but not the first
choose the max result

edge cases:
1. not nums
2. only has one house -> after delete the first/last house, the nums is []
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        if not nums:
            return 0
        
        rob, not_rob = nums[0], 0
        
        for i in range(1, len(nums)):
            rob, not_rob = not_rob + nums[i], max(rob, not_rob)
        
        return max(rob, not_rob)    

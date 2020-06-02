You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

    
'''
dp[i] means for curt house i, all the money the robber robbed

dp[i][0] for curt i house, not rob
dp[i][1] for curt i house, rob

dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
dp[i][1] = dp[i - 1][0] + nums[i] #if house i will rob -> house i - 1 cannot rob
'''
#time: O(n), space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        #dp的初始化。注意写法！！
        dp = [[0,0] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        
        return max(dp[-1][0], dp[-1][1])

      
#time: O(n), space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        rob, not_rob = nums[0], 0
        
        for i in range(1, len(nums)):
            #利用python特性
            rob, not_rob = not_rob + nums[i], max(not_rob, rob)
            
        return max(rob, not_rob)

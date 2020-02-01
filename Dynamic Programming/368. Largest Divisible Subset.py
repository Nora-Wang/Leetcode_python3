Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]


DP模板

code:
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        
        #需要提前排序,满足递增序列
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i):
                #这里是直接满足连续性的,即eg:[1,2,4,8], 只要4 % 2 = 0就能满足4 % 1 = 0
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        prev[i] = j
        
        path = []
        index = dp.index(max(dp))
        
        while index != -1:
            path.append(nums[index])
            index = prev[index]
        
        return path[::-1]
            
            

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

解析：
实际上就是求是否存在子数组，使得子数组的和等于整个数组和的1/2。考虑用动规，看成是0-1背包问题的一种变形，dp[i][j]表示考虑前i个数字，
是否存在子数组和为j。

转移方程为dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]（即不选第i个数字或者选第i个数字）

可以用滚动数组进行优化。

时间复杂度: O(MN). M是数组元素和，N是数组元素个数

参考链接：https://www.acwing.com/solution/LeetCode/content/6416/

code:
'''
step 1: set
find a subset that sum is target(all_sum // 2)
dp[i][j]: i means the previous i numbers; j means curt subset sum
dp[i][j]表示考虑前i个数字，是否存在子数组和为j

step 2: attribute
count

step 3:
pick it or not pick it
dp[i] -> dp[i - 1][j], dp[i - 1][j - nums[i]]
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        
        if all_sum % 2:
            return False
        
        target = all_sum // 2
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(0, len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] |= dp[j - nums[i]]
        
        return dp[target]


'''
DFS recursion code
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
    
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        return self.help(nums, 0, target)
    
    def help(self, nums, index, target):
        if index >= len(nums) or target < 0:
            return False
        
        if target == 0:
            return True
        
        return self.help(nums, index + 1, target) or self.help(nums, index + 1, target - nums[index])


'''
二维DP写法

实际上就是求是否存在子数组，使得子数组的和等于整个数组和的1/2。考虑用动规，看成是0-1背包问题的一种变形，dp[i][j]表示考虑前i个数字，
是否存在子数组和为j。

转移方程为dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]（即不选第i个数字或者选第i个数字）

时间复杂度: O(MN). M是数组元素和，N是数组元素个数
空间复杂度: O(MN)

参考链接：https://www.acwing.com/solution/LeetCode/content/6416/
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
    
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len(nums)][target]

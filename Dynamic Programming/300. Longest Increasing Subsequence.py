Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


O(n2) 解法： 
Dp[i] 表示以第i个数字为结尾的最长上升子序列的长度。 
对于每个数字，枚举前面所有小于自己的数字 j，Dp[i] = max{Dp[j]} + 1. 如果没有比自己小的，Dp[i] = 1; 
    
code:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #初始化所有最长子序列都为1
        dp = [1] * len(nums)
        
        #遍历nums里的每一个点
        for i in range(1,len(nums)):
            #遍历当前点之前的所有点 
            for j in range(i):
                #如果之前点的值小于当前点的值，就要考虑加入dp 
                #如果之前点的递增长度加上1（当前点）,小于当前点的已有的递增长度，则不更新递增长度 
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)
        

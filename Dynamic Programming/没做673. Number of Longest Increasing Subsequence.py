Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.




code:
class Solution: 
    def findNumberOfLIS(self, nums: List[int]) -> int: 
        if not nums: 
            return 0 
         
        #dp[i] = [x, y] x代表以i为结束点的最长长度 y代表以i为结束点的最长长度的数量 
        dp = [[1, 1] for _ in range(len(nums))] 
         
        for curt in range(len(nums)): 
            for prev in range(curt): 
                #如果是递增的在进入循环 
                if nums[prev] < nums[curt]: 
                    #如果prev+1的长度大于curt，此时更新curt的长度 
                    if dp[curt][0] < dp[prev][0] + 1: 
                        dp[curt] = [dp[prev][0] + 1, dp[prev][1]] 
                    #如果两个长度相等，更新curt的位置的数量（当前的数量加上之前的数量） 
                    elif dp[curt][0] == dp[prev][0] + 1: 
                        dp[curt][1] += dp[prev][1] 
                        
        #数一下长度为最长的的子串有多少个 
        count = 0                 
        max_value = max(dp, key=lambda x: x[0]) 
         
        for l, num in dp: 
            #遇到长度为最长的子串，记录其个数，本题记录4的个数，4可能在不同的地方 
            if l == max_value[0]: 
                count += num 
                         
        return count 

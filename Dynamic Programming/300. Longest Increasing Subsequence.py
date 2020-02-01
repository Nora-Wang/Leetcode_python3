Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


坐标型DP
    
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
        

#输出path
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # state: dp[i] 表示从左到右跳到i的最长sequence 的长度
        
        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)
        
        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)
        
        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i
        
        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])
        
        return longest

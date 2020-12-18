Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

    
# 12/18/2020
# time: O(n), space: O(n)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        
        min_nums = [float('inf')] * len(nums)
        for i in range(1, len(nums)):
            min_nums[i] = min(min_nums[i - 1], nums[i - 1])
            
        max_nums = [float('-inf')] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            max_nums[j] = max(max_nums[j + 1], nums[j + 1])
            
        for i in range(1, len(nums) - 1):
            if min_nums[i] < nums[i] < max_nums[i]:
                return True
        
        return False
    
    
    
    
    

code:
#DP Version
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    if dp[i] == 3:
                        return True
        
        return False
        
        
# time: O(n), space: O(1)        
#直接解
#只要能找到3个数,first < second < last,即说明成立
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first, second = sys.maxsize, sys.maxsize
        
        for num in nums:
            #因为题目要求irst < second < last,因此这里为<=,意思是second一定大于first
            #找到第一个最小值
            if num <= first:
                first = num
            
            #找到第二个最小值,满足second > first
            elif num <= second:
                second = num
            
            #找到第三个最小值,满足 last > second > first
            else:
                return True
        
        return False

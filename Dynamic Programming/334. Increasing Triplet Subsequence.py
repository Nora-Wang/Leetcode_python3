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

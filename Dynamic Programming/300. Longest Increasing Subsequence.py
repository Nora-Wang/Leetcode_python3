Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


code:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        record = [1] * len(nums)
        result = 1
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    record[i] = max(record[j] + 1, record[i])
                    
            result = max(result, record[i])
        
        return result
        

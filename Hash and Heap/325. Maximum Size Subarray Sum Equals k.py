Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?


code:
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        # record = {prefix_sum:index}
        record = collections.defaultdict(int)
        record[nums[0]] = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            record[nums[i]] = i
        
        res = 0
        # include nums[0]
        if k in record:
            res = record[k] + 1
        
        for i in range(len(nums)):
            if (nums[i] + k) in record:
                res = max(res, record[nums[i] + k] - i)
        
        return res

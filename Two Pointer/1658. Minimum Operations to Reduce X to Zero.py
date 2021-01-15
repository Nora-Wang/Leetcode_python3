You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109

# 找到中间最长的sum = sum(nums) - x的subarray即可
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        l, r = 0, 0
        curt_sum = 0
        max_subarray = -1
        while l < len(nums):
            while r < len(nums) and curt_sum < target:
                curt_sum += nums[r]
                r += 1
            
            if curt_sum == target:
                max_subarray = max(max_subarray, r - l)
            
            curt_sum -= nums[l]
            l += 1
        
        return -1 if max_subarray == -1 else len(nums) - max_subarray

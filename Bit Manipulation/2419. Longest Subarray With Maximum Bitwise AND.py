You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106


# One loop
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/discuss/5783278/Find-1st-location-for-max-then-find-successive-maxoror41-ms-Beats-99.34
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len, max_sub, length = 0, 0, 0
        n = len(nums)
        i = 0
        
        while i < n:
            while i < n and nums[i] == max_sub:
                i += 1
                length += 1
            
            if i == n or nums[i] < max_sub:
                max_len = max(max_len, length)
                length = 0
            else:
                max_sub = nums[i]
                max_len = length = 1
            
            i += 1


# Two loop
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/discuss/5771401/Best-Solution-oror-Easy-Explanation-oror-All-languages
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 1st loop
        max_val = max(nums)
        length = 0
        
        # 2nd loop
        count = 0
        for num in nums:
            if num == max_val:
                count += 1
                length = max(length, count)
            else:
                count = 0
        
        return length
        
        return max_len

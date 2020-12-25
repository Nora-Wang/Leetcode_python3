Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if len(nums) < k or total % k:
            return False
        
        side = total // k
        nums.sort(reverse=True)
        return self.helper(nums, 0, [0] * k, side, k)
    
    def helper(self, nums, index, record, side, k):
        if index == len(nums):
            for c in record:
                if c != side:
                    return False
            return True
        
        for i in range(k):
            if record[i] + nums[index] <= side:
                record[i] += nums[index]
                if self.helper(nums, index + 1, record, side, k):
                    return True
                record[i] -= nums[index]
        
        return False

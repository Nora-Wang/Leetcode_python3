Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


'''
clarification:
input: None? []? negative? array with int?
output: int

1. brute force
use 2 for loop to list all the possible subarray, compare the products one by one
    result = nums[0]
    for i in range(len(nums)):
        accu = 1
        for j in range(i, len(nums)):
            accu *= nums[j]
            result = max(result, accu)
time: O(n^2), space: O(1)

2. optimal
smaller problem:
    for index = i - 1, max_p, min_p
    if nums[i] > 0 -> [min_p * nums[i], max_p * nums[i]]
    if nums[i] < 0 -> [max_p * nums[i], min_p * nums[i]]
    max_p = max(nums[i], max_p * nums[i], min_p * nums[i])
    min_p = min(nums[i], min_p * nums[i], max_p * nums[i])

    res = max(res, max_p)
    
initail:
    max_p, min_p, res = nums[0]

time: O(n), space: O(1); n = len(nums)

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_p = nums[0] # the largest product for curt index
        min_p = nums[0] # the smallest product for curt index
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            temp = min_p
            min_p = min(min_p * nums[i], max_p * nums[i], nums[i])
            max_p = max(max_p * nums[i], temp * nums[i], nums[i])
            
            res = max(res, max_p)
        
        return res
        
        

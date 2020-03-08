Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


code:
Version 1:错位dislocation
[1, 1, 2, 6]
[24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = [1] * len(nums)
        left, right = 1, 1
        
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]
        
        return res


Version 2:
l_r: [1, 2, 6, 24]
r_l: [24, 24, 12, 4]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        l_r = []
        left = 1
        r_l = []
        right = 1
        
        for i in range(len(nums)):
            left *= nums[i]
            right *= nums[len(nums) - 1 - i]
            
            l_r.append(left)
            r_l.append(right)
        
        r_l.reverse()
        
        res = [None] * len(nums)
        res[0] = r_l[1]
        res[-1] = l_r[-2]
        for i in range(1, len(nums) - 1):
            res[i] = l_r[i - 1] * r_l[i + 1]
        
        return res

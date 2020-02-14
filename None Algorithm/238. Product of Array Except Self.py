Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


类似题目参考724

code:
#模板1
#这里left存的值是prefix的积,right存的值是该值后面的所有值的积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = [1 for _ in nums]
        
        left = 1
        for i in range(len(nums)):
            result[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result



#模板2
#这里的left存的是prefix的积*当前值,right存的是当前值*后续所有值的积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        left = [_ for _ in nums]
        right = [_ for _ in nums]
        
        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]
        
        #case处理
        result = [None] * len(nums)
        result[0] = right[1]
        result[-1] = left[-2]
        for i in range(1, len(nums) - 1):
            result[i] = left[i-1] * right[i+1]
        
        return result

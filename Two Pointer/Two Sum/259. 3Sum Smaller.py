Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?


3sum不去重模板

code:
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        result = 0
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                value = nums[left] + nums[right] + nums[i]
                
                if value < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
                    
        return result

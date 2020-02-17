Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

code:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        #一定要记得sort
        nums.sort()
        res = []
        
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i-1]:
                continue
            
            curt_target = target - nums[i]
            #注意这里的j的取值范围
            for j in range(i+1, len(nums)-2):
                #这里j要对应上面的取值范围
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    value = nums[left] + nums[right] + nums[j]
                    
                    if value == curt_target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    
                    elif value < curt_target:
                        left += 1
                    else:
                        right -= 1
        
        return res
        

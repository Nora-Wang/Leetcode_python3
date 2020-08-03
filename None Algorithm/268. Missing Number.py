Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


# 08/02/2020
# Math Version
# time: O(n), space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        correct_sum = (0 + n) * (n + 1) // 2
        
        return correct_sum - sum(nums)
    
    
# Sort Version
# time: O(nlogn), space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for index, num in enumerate(nums):
            if index != num:
                return index
        
        return len(nums)

# HashSet Version
# time: O(n), space: O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in set_nums:
                return i
        
# List Index Version
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 保证n也能被find，而不会out of index
        nums.append(1)
        
        # 用于记录index：nums[index] = 0。因为0 * -1 = 0
        mark_0 = 0
        
        # 排除最后一位，因为是自己加的
        for i in range(len(nums) - 1):
            # 当出现0，则mark位置，再将nums[0] * -1，以标记0在nums中出现过
            if nums[i] == 0:
                mark_0 = i
            
            nums[abs(nums[i])] *= -1
        
        for index, num in enumerate(nums):
            if num > 0:
                return index
        
        # 若所有数都标为负数了，则证明只有nums[index] = 0，即index这个值miss
        return mark_0

    
    

code:
一旦遇到list中数据与index有关的,都可以考虑将它们结合起来做,即将nums[abs(nums[i])] *= -1
#通用解法
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #这一步能使得n也能被mark,避免*-1时出现out of index
        #append不会产生新的list
        nums.append(len(nums))
        
        #用于记录当前nums[abs(nums[i])]值为0的情况
        record_zero = 1
        
        for i in range(len(nums) - 1):
            #若当前nums[abs(nums[i])]为0,则mark一下,这样后续在review这个index的时候好判断到底该点有没有被赋值过
            if nums[abs(nums[i])] == 0:
                record_zero = -1
                continue
            
            #可能会出现重复数据
            if nums[abs(nums[i])] < 0:
                continue
            
            nums[abs(nums[i])] *= -1
        
        for i in range(len(nums)):
            #该点为0,且没有被Mark
            if nums[i] == 0 and record_zero == 1:
                return i
            
            if nums[i] > 0:
                return i
        
    
    
    
    
#brute force
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return nums[-1] + 1
            

题目：
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].


# 09/08/2020
# time: O(logn), space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        
        if first != -1 and last != -1:
            return [first, last]
        if first != -1 or last != -1:
            return [max(first, last), max(first, last)]
        return [-1, -1]
    
    def find_first(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def find_last(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1




这题可以好好研究，主要思路是需要分别找到target第一次出现的位置和最后一次出现的位置，返回即可。
套用模板的时候，每一步骤要分析清楚！！！尤其是while循环和最后的if(end/start)语句！！

code：
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        result = [-1,-1]
        
        #find start index
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            result[0] = start
        elif nums[end] == target:
            result[0] = end
        else:
            #if cannot find the start index, which means the target do not exist in the nums, so return [-1,-1]
            return result
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[end] == target:
            result[1] = end
        ##attention: use elif not if, because the nums[start] may equals to nums[end]
        elif nums[start] == target:
            result[1] = start
            
        return result

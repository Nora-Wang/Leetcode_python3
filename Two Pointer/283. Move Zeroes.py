Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.




Ask HR what's mean of 'Minimize the total number of operations.'?
Minimize对nums的修改次数，即最小化写操作

code:
Version 1
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        quick, slow = 0, 0
        
        while quick < len(nums):
            if nums[quick] != 0:
                nums[slow], nums[quick] = nums[quick], nums[slow]
                slow += 1
            quick += 1
            
            

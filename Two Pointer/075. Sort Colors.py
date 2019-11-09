Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


思路：
三个指针，left和right用于设置阵营，index用于遍历所有数值
当index为0时,与left交换,即将0放到左侧;
当index为2时,与right交换,即将2放到右侧;
当index为1时,skip
这样可以满足左侧是0,右侧是2,中间是1


code:
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        if not nums:
            return
            
        ##三个指针，left和right用于设置阵营，index用于遍历所有数值
        left, right, index = 0, len(nums) - 1, 0
        
        # #index碰到right前都可以遍历
        while index <= right:
            #如果当前值是2,放到最右,右指针往左挪,index不用动,因为不知道此时index的值是1还是0,需要继续判断这个值
            if nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
                
            #如果当前值是0,放到最左,左指针往前挪,index往前走
            #这里index必须往前挪,否则会报错.因为如果不挪,index会一直停留在该点,导致死循环
            #这里注意，由于nums[index] == 2的情况时,index不能挪动,因此不是每种情况都能index += 1,即不能在while循环的最后直接写index += 1,
            #所以在nums[index] == 0中需要单独写一次
            elif nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            
            #如果是1,则跳过,index往前走
            else:
                index += 1
                


Version 2:去重版
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        left, right, index = 0, len(nums) - 1, 0
        
        while index <= right:
            if nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
                #将right为2的情况去重
                while index <= right and nums[right] == 2:
                    right -= 1
                
                
            elif nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
                #将left为0的情况去重
                #注意这里index也要挪动
                while index <= right and nums[left] == 0:
                    left += 1
                    index += 1
            else:
                index += 1
                

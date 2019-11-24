Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?



code:
Version 0:

###########知识点###########
Slice
nums[::-1]反转nums
nums[::2]每两个取一个值
nums[-1:]取值nums的最后一个值(前面的数一定要比后面的小)
nums[-1:-3:-1]先是取值nums的倒数第二个值和倒数第一个值(这里的方向是从最后一个值向倒数第二个值取值),然后-1代表反向即从倒数第二个值向最后一个值取值
###########################

nums[:]代表深拷贝
因为可以倒着去值,因此k可以不用取余
nums[len(nums) - k:]代表新建一个list,其取值为nums的index为len(nums) - k到len(nums) - 1
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        
        
Version 1:
逻辑为先将整个list翻转,然后将前k位翻转,再将后面的翻转
reverse是start和end直接换就行,一直到start和end相遇即可
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        
        self.reverse(nums, 0, k - 1)

        self.reverse(nums, k, len(nums) - 1)
    
    #自写一个reverse
    #必须使用start和end
    #若用self.reverse(nums[0:k]),nums[0:k]还是相当于新建了一个list,原始的nums还是没变
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.




Ask HR what's mean of 'Minimize the total number of operations.'?
Minimize对nums的修改次数，即最小化写操作


Version 1: 基于 swap 的版本
这种方法无法保证写次数最小，因为在swap的过程中,0会被不断的换在不同的位置上,这样就造成了步骤重复

demo:
初始化
[0,1,0,3,12]
 q
 s

swap过程
[0,1,0,3,12] => [1,0,0,3,12] => [1,0,0,3,12] => [1,0,0,3,12] => [1,3,0,0,12] => [1,3,0,0,12] => [1,3,12,0,0]
 s q             s q               s q             s   q           s   q             s    q           s   q
  q + 1          s与q的值交换     s + 1,q + 1        q + 1        s与q的值交换      s + 1,q + 1     s与q的值交换
                 2次写操作                                          2次写操作                       2次写操作

综上,一共2+2+2=6次写操作
    
    
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
            
      
    
Version 2:这个版本可以保证最小的“写”次数
demo:
初始化
[0,1,0,3,12]
 q
 s

replace过程
[0,1,0,3,12] => [1,1,0,3,12] => [1,1,0,3,12] => [1,1,0,3,12] => [1,3,0,3,12] => [1,3,0,3,12] => [1,3,12,3,12]
 s q             s q               s q             s   q           s   q             s    q           s   q
  q + 1          将q值赋值给s     s + 1,q + 1        q + 1        将q值赋值给s      s + 1,q + 1     将q值赋值给s
                 1次写操作                                          1次写操作                        1次写操作
此时q到nums的尾部,退出循环,再用2次写操作,将s后面的非0值赋值为0

综上,一共1+1+1+2=5次写操作
    
    
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        quick, slow = 0, 0
        #将q赋值给s
        while quick < len(nums):
            if nums[quick] != 0:
                if slow != quick:
                    nums[slow] = nums[quick]
                slow += 1
            quick += 1
            
        #将s后面的非0数赋值为0
        #注意，因为要求写操作最小，所以需要判断是否为0，再进行赋0的写操作；若直接用while循环,每个值都赋值为0,当其本身就为0时,会增加冗余的写操作
        while slow < len(nums):
            if nums[slow] != 0:
                nums[slow] = 0
            slow += 1
        
            
            

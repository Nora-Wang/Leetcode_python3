题目：
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.


不清楚可以画图：
              ↗
            ↗
          ↗
        ↗
      ↗
    ↗
  ↗
↗
旋转数组，分成两段上升数组：
              ↗|
            ↗  |
          ↗    |
        ↗      |
      ↗        |
---------------|------------------
               |    ↗
               |  ↗
               |↗
      ↑     ↑        ↑
    start  mid      end
    
    
    
    
注意：可以利用min()函数简化程序






code：

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #initial version
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if(nums[mid] < nums[start]):
                end = mid
            else:
                start = mid
        #需要考虑nums[0]的情况，即全部都是递增的；这时候再执行上述代码，得到的结果应为最大值
  #错误点
        return min(nums[0], nums[end], nums[start])
  
  
  
######第二次做，方法没问题，就是太慢了
  class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return -1
        start = 0
        end = len(nums) - 1
        while(start + 1 < end):
            mid = start + (end - start) - 1
            if(nums[start] > nums[end]):
                if(nums[mid] > nums[end]):
                    start = mid
                else:
                    end = mid
            else:
                return nums[start]
        if(nums[start] > nums[end]):
            return nums[end]
        else:
            return nums[start]
                    
        
lintcode version
version 1更简洁:
  class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        
        start = 0
        end = len(nums) - 1
        
        if nums[start] < nums[end]:
            return nums[start]
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])

      
version 2:
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        
        start = 0
        end = len(nums) - 1
        
        if nums[start] < nums[end]:
            return nums[start]
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= nums[end] < nums[start]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

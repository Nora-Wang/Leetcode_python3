题目：
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.


不清楚点可以画图：
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

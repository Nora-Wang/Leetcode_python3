题目：
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.



这道题思路简单，主要是情况较多，需要考虑完全

Note:发现规律
target > nums[mid]
r > x
固定数据（传入数据/计算得出的数据） > 二分边界数据


Code:
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
     #version 1
        l = 0
        size = len(nums)
        r = size - 1
        #nums为空
        if size == 0:
            return size
        #nums为单元素列表or target比第一个元素小
        if target <= nums[0]:
            return 0
        #target比最后一个元素大
        elif target > nums[-1]:
            return size
        else:
            while(l < r):
                mid = (l + r) / 2
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            return r
        #T(n) = n
        
      #version 2(简化版，减去部分特殊判断)
        size = len(nums)
        l, r = 0, size - 1
        if size == 0 or target > nums[-1]:
            return size
        while(l < r):
            mid = (l + r) / 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return r
        
      #九章version
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        #分析当找不到target时的情况
        #target <= nums[start](最小) or target <= nums[end](介于start和end之间) or target > nums[end](最大)
  #易错点：start与end的顺序，从小比到大
        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1
        




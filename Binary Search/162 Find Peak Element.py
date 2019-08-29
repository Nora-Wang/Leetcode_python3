A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.



思路：
1. 九章
分四种情况分析：m在peak处；m在下坡处，即左侧一定有peak；m在上坡处，即右侧一定有peak；m在坡底

2. 简易版
因为题目要求any one of the peaks，因此可将整体看作一个坡，求其peak

3.要求nums[i] ≠ nums[i+1]是因为会出现[1,2,3,3,3,2,1]的情况，不满足所分析的四种情况。若问[2,2,2,1,2,2,2],则直接用for循环,不需要二分



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #九章version
        if (len(nums) == 1):
            return 0
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            #m在peak处
            if (nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]):
                return mid
            #m在下坡处，即左侧一定有peak
            elif (nums[mid - 1] > nums[mid] > nums[mid + 1]):
                end  = mid
            #m在坡底，两侧随意选择
            elif (nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]):
                start = mid
            #m在上坡处，即右侧一定有peak
            else:
                start = mid
        if(nums[start] > nums[end]):
            return start
        else:
            return end

        #简易version
        #思路：可看作只有一个坡，求其peak
        if (len(nums) == 1):
            return 0
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if (nums[mid + 1] > nums[mid]):
                start = mid
            else:
                end = mid
        if (nums[start] > nums[end]):
            return start
        else:
            return end




题目：
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].


这题可以好好研究，主要思路是需要分别找到target第一次出现的位置和最后一次出现的位置，返回即可。
套用模板的时候，每一步骤要分析清楚！！！尤其是while循环和最后的if(end/start)语句！！

code：

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
 #九章version
        result = [-1, -1]
        if len(nums) == 0:
            return result
        #找first position
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                #找first position，即找target第一次出现的位置，所以限制end
                end = mid
            else:
 ####第二次做改良版：start = mid + 1
                start = mid
        #需要考虑清楚，只剩最后两个数据的时候，若为[1, 1], 因为找first position，所以应先查看start，再查看end
        if nums[start] == target:
            result[0] = start
        elif nums[end] == target:
            result[0] = end
 ####第二次做改良版：若循环一遍都找不到target，那直接return result
#         else:
#             return result

        #找second position
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                #找second position，即找target最后一次出现的位置，所以限制start
                start = mid
            else:
 ####第二次做改良版：end = mid - 1
                end = mid
        # 需要考虑清楚，只剩最后两个数据的时候，若为[1, 1], 因为找second position，所以应先查看end，再查看start
        if nums[end] == target:
            result[1] = end
        elif nums[start] == target:
            result[1] = start
        return result

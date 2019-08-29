题目：
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.


思路：
抽屉问题
1.仔细理解题意，从共n+1个数，取值范围：1～n(包括n)，即最大值为n
2.m = (1 + n) / 2。设有共有n个抽屉,用count记录被放在1～m抽屉中的苹果数目。
若苹果树count<=抽屉数m，则说明1~m抽屉有空或每个都有一个苹果；即 m～n抽屉的苹果数 > 1~m抽屉的苹果数 ==>左边界left=m


left__________________________________mid___________right
    mid-left+1个抽屉  vs   count个苹果




code:

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = len(nums) - 1
        i = 0
        while(left < right):
            mid = left + (right - left) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if(count <= mid):
                left = mid + 1
            else:
                right = mid
        return right
                
        

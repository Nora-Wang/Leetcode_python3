题目：
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.


# 09/08/2020
'''
0. brute force: for every num, find is there has duplicate num in array
time: O(n^2), space: O(1)

1. sort, walk though the nums to find the duplicate number
time: O(nlogn), space: O(1)/O(n)

2. set, walk though the nums to find the duplicate number
time: O(n), space: O(n)

3. utilize index to modify the array nums: 
for every num in the nums:
      if nums[abs(num)] > 0 -> mark nums[abs(num)] = - nums[abs(num)] 
      if nums[abs(num)] > 0 -> abs(num) is the duplicate number
time: O(n), space: O(1)

4. binary search
base on this information: nums containing n + 1 integers where each integer is in the range [1, n] inclusive
do binary search on the integer's range [1,n] -> left, right = 1, n
varify go left or right based on how many numbers in nums are <= mid -> count
if count <= mid -> go to right side
if count > mid -> go to left side
time: O(nlogn), space: O(1)
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count > mid:
                right = mid
            else:
                left = mid
        
        # 需要再用一个for循环计算nums中有多少个数小于count，才能判断最后结果是left还是right
        count = 0
        for num in nums:
            if num <= left:
                count += 1
        
        return right if count <= left else left
        
        
# 更优写法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        
        # 这里停止的条件就是left == right
        while left < right:
            mid = (left + right) // 2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # 当出现count <= mid时，则说明duplicate number一定出现在[mid + 1:right]里，因此可以left + 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return left







思路：
抽屉问题
1.仔细理解题意，从共n+1个数，取值范围：1～n(包括n)，即最大值为n
2.m = (1 + n) / 2。设有共有n个抽屉,用count记录被放在1～m抽屉中的苹果数目。
若苹果树count<=抽屉数m，则说明1~m抽屉有空或每个都有一个苹果；即 m～n抽屉的苹果数 > 1~m抽屉的苹果数 ==>左边界left=m


left__________________________________mid___________right
    mid-left+1个抽屉  vs   count个苹果



###这里要注意mid是指1～n值的mid，不是array的mid，因此对于mid存在的数组来说就是sorted的（这里的left和right都是用于计算mid的取值范围，不是用于定位）
#在计算count的时候才是在真正给的array里计算
##这道题本质上就是在比较array里面有多少个值(count)是比中位数(mid)大的，如果个数比中位数多，那就证明重复的值在1～中位数之间，反之则在中位数～n之间
code:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count <= mid:
                start = mid + 1
            else:
                end = mid
        
        return start
                
        

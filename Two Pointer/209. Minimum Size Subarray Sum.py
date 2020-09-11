Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


# 09/11/2020
'''
1. brute force
for every num find the minimum size subarray
time: O(n^2), space: O(1)

2. binary search
get the sum_nums array
utilize binary search to find the minimum size subarray for every num
target = sum_nums[i] + s - nums[i]
start, end = 0, len(nums) - 1
nums[mid] < target -> start = mid
nums[mid] >= target -> end = mid

time: O(nlogn), space: O(n)

3. sliding window / two pointer
use left to represent the size of curt subarray window
use curt_sum to represent curt sum for this subarray

use for loop to caculate the sum of the subarray
    while curt_sum >= s:
        renew res -> min
        renew curt_sum -> curt_sum -= nums[left]
        renew left -> left += 1
    
time: O(n), space: O(1)

'''
# binary search
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        
        sum_nums = [nums[0]]
        for i in range(1, len(nums)):
            sum_nums.append(nums[i] + sum_nums[i - 1])
        
        res = len(nums)
        for i in range(len(nums)):
            target = sum_nums[i] + s - nums[i]
            
            end_index = self.binary_search(sum_nums, target)
            
            if end_index == -1:
                continue
            
            res = min(res, end_index - i + 1)
        
        return res
    
    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return -1


# sliding window
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left, res, sum = 0, len(nums) + 1, 0
        
        for i in range(len(nums)):
            sum += nums[i]
            
            while sum >= s:
                res = min(res, i - left + 1)
                sum -= nums[left]
                left += 1
        
        return res if res != len(nums) + 1 else 0
    
    
    
    




最坏解法:i,j循环n次,O(n^2)

算法强化班解法:同向双指针问题,i从头到尾的遍历;而j从i=0的时候遍历到满足sum>=s的时候,然后把i=0的值从sum中删除,然后再继续寻找能使sum>=s的j的值;
整个过程i遍历了整个nums,j也是只遍历一遍nums;因此为O(n)

code:
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        j = 0
        #初始值设为最大,后面好取最小值
        min_length = sys.maxsize
        
        for i in range(len(nums)):
            #找到第一个满足sum >= s的j
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            
            #可能存在一种情况:从nums的i到len(nums) - 1的sum < s;这种时候直接跳过即可;只有当满足sum>=s的条件时,才将j-i记录
            if sum >= s:
                #注意上一个while循环结束时,j的值为满足sum >= s的j的下一个,即j+1;因此这里为j-i
                min_length = min(min_length, j - i)
            
            #每一次循环的最后都需要将当前的nums[i]去掉,这样才能找下一轮
            sum -= nums[i]
        
        #当找不到时,eg:nums = [1,2], s = 10
        if min_length == sys.maxsize:
            return 0
        
        return min_length

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 



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

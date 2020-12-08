Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

# 12/08/2020
# time: O(n), space: O(1)
# n = len(nums)
# prev: the first exist num; num: the last exist num -> missing num in range (prev + 1 ~ num - 1)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.append(upper + 1)
        res = []
        prev = lower - 1
        
        for num in nums:
            # == 2 -> only one missing num
            if num - prev == 2:
                res.append(str(prev + 1))
            elif num - prev > 2:
                res.append(str(prev + 1) + '->' + str(num - 1))
            prev = num
            
        return res    
    
    
    
    
    
    
    
思路:模拟题,没什么算法;注意corner case,注意last的定义


code:

Version 1 高频班java直接翻译版 8ms
class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        #corner case
        if not len(nums):
            #注意输出结果的格式,需要加[]
            return [self.create_range(lower, upper)]
        
        result = []
        #注意last的设计,这里的last只的是目前能取到的最小值(与Version 3做对比)
        last = lower
        
        for i in range(len(nums)):
            #case: nums = [0, 1], lower = 2
            if last >= nums[i]:
                #因为last的定义,这里需要+1
                last = nums[i] + 1
                continue
            #因为create_range函数的start和end表示能取到的最小值与最大值,因此end在取值时应为nums[i] - 1
            result.append(self.create_range(last, nums[i] - 1))
            
            #注意每次循环结束时都要将last重新赋值,注意+1
            last = nums[i] + 1
        
        #case: nums = [0, 1], upper = 4;结果为["2->4"]
        #case: nums = [0, 1], upper = 2;结果为["2"]
        #此时的last是nums的最后一个值+1,当它还<=upper时,证明还有最后一截corner case需要加入result
        if last <= upper:
            result.append(self.create_range(last, upper))
        
        return result
        
    def create_range(self, start, end):
        if start == end:
            return str(start)
        #另一种写法:return str(start) + '->' + str(end). 缺点:慢
        return '{}->{}'.format(start, end)
        

Version 2 高频班简化版 12ms
class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        if not len(nums):
            return [self.create_range(lower, upper)]
        
        result = []
        last = lower
        #直接将upper + 1加入nums,省去最后对upper与last的判断
        nums.append(upper + 1)
        
        for i in range(len(nums)):
            if last >= nums[i]:
                last = nums[i] + 1
                continue
            result.append(self.create_range(last, nums[i] - 1))
                
            last = nums[i] + 1
        
        return result
        
    def create_range(self, start, end):
        if start == end:
            return str(start)
        return '{}->{}'.format(start, end)
        
        
Version 3 大神版
可以把nums里的数看成是障碍物，其实是求两障碍物之间的区间。为了保证所求区间在[lower,upper]之间，
可以在lower-1和upper+1的位置上各放一个障碍物。从第一个障碍物起，每次碰到新的障碍物的时候去跟之前的障碍物的位置比较：
1）若前一障碍物的位置是当前障碍物位置-2，那么这两个障碍物之间只有有一个数；
2）若前一障碍物的位置<当前障碍物位置-2，那么这两个障碍物之间只有若干(>2)个数；
3）若前一障碍物的位置是当前障碍物位置-1，也就是不满足1）和2），那么继续下一个障碍物；
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        #这里的last表示能取到的最小值-1
        result, last = [], lower - 1
        nums.append(upper + 1)
        
        for cur in nums:
            diff =  cur - last
            if diff == 2:
                result.append(str(cur - 1))
            elif diff > 2:
                result.append("{}->{}".format(last + 1, cur - 1))
                
            #因为last的定义,因此last直接等于nums[i]即这里的cur即可
            last = cur
                
        return result

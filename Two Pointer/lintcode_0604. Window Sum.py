Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example

Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20


这个问题并没有什么难度，但是如果你过于暴力的用户O(n∗k) 的算法去做是并不合适的。
比如当前的 window 是 |1,2|,3,4。那么当 window 从左往右移动到 1,|2,3|,4 的时候，整个 window 内的整数和是增加了3，减少了1。
因此只需要模拟整个窗口在滑动的过程中，整数一进一出的变化即可。这就是滑动窗口问题。


知识点：python初始化指定长度的一维list
1.方式一
a = [None] * n
2.方法二
a = [None for i in range(n)]


code:
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums or k == 0:
            return []
            
        result = [] * (len(nums) - k + 1)
        
        sum_record = 0
        for i in range(k):
            sum_record += nums[i]
        
            
        for i in range(len(nums) - k):
            result.append(sum_record)
            sum_record = sum_record - nums[i] + nums[i + k]
            
        result.append(sum_record)
        
        return result
        
        

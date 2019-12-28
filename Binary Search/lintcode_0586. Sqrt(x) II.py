Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

Example

Example 1:

Input: n = 2 
Output: 1.41421356
Example 2:

Input: n = 3
Output: 1.73205081
Notice

You do not care about the accuracy of the result, we will help you to output results.



思路: 二分法


code:
class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x == 0:
            return 0
        
        if x >= 1:
            start, end = 1, x
        else:
            start, end = x, 1
        
        #注意python的浮点数写法:1e2 = 100.0000....
        #这道题bug是没有写明到底要保留多少位,1e-12/1e-10都行,但数值太大时会超时
        while start + 1e-12 < end:
            mid = start + (end - start) / 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                start = mid
            else:
                end = mid
        
        #这个地方因为前面的浮点数1e-12只有12位,导致算到最后时start == end,就不需要做比较了
        return start
        
        '''if end ** 2 <= x:
            return end
        else:
            return start'''

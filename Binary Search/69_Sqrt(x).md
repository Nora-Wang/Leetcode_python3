题目：
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.



Question:
为什么不能是result >= x or result < x????

Code:
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #initial version
        self.x = x
        if self.x >= 0:
            y = x ** 0.5
            return y
        
        #version 1: result > x
        l, r = 0, x
        while(l < r):
            mid = (l + r + 1) / 2
            result = mid * mid
            if(result > x):
                r = mid - 1
            else:
                l = mid
        return l
        #T(n) = n    

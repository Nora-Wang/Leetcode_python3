#题目：
#Implement int sqrt(int x).

#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.



#Question:
#为什么不能是result >= x or result < x????



code:
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
        
        #九章version
        if x == 0:
            return 0
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                start = mid
            else:
                end = mid
        #根据题目判断end在前
        if end ** 2 <= x:
            return end
        else:
            return start
        return 0

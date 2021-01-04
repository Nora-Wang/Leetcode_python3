#题目：
#Implement int sqrt(int x).

#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.


# 1/4/2020
# Version 1: Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x 

        while start + 1 < end:
            mid = (start + end) // 2

            if mid**2 == x:
                return mid
            if mid**2 < x:
                start = mid
            else:
                end = mid
                
        return end if end**2 <= x else start
    
# Version 2: recursion + bit manipulation   
# sqrt(x) = 2 * sqrt(x // 4)
# x << y = x * 2^y
# x >> y = x // 2^y
# -> sqrt(x) = sqrt(x >> 2) << 1
# time: O(logn), space: O(logn) for recursion
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1 # eg: x = 2, left = 1, right = 2
        
        return left if right**2 > x else right



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

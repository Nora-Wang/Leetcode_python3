Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

code:
leetcode version
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #特判
        if x == 1 or n == 0:
            return 1
        #当n为负数时
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        temp = x
        while n:
        #n为奇数时eg:n=5，result = temp，即result = x，这时因多的一个x已被记录进result，所以n的值会变成偶数,即n=4
        #接下来就是两两组对，将剩余的值都赋给temp=x^4
        #****当n为1时，又会进入if语句，这时就会将之前算的x^4再乘给result，即result=x * x^4
            if n % 2:
                result *= temp
                n -= 1
            temp *= temp
            n /= 2
        return result
        
        
        
lintcode version:
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n == 0 or x == 1:
            return 1
            
        if n < 0:
            x = 1 / x
            n = abs(n)
            
        temp = x
        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= temp
                n -= 1
            temp *= temp
            n /= 2
        return result
        

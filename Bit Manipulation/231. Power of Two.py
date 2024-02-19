Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?


# Method 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            cur = 2**i
            if cur == n:
                return True
        
        return False

# Method 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 2 == 0:
            n //= 2
        
        return n == 1

# Method 3
# Bit
# Explanation: https://leetcode.com/problems/power-of-two/discuss/1638704/C%2B%2B-EASY-TO-SOLVE-oror-All-INTERVIEW-APPROACHES-with-Detailed-Explanations
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return (n & (n-1)) == 0

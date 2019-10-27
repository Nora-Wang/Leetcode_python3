Calculate the a^n % b where a, b and n are all 32bit non-negative integers.

Example

For 2^31 % 3 = 2

For 100^1000 % 1000 = 0

Challenge

O(logn)


思路：
主要利用公式：(a * b) % p = ((a % p) * (b % p)) % p 
运用recursion的思路


code:
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        #特判
        if n == 0:
            return 1 % b
        
        #recursion最底层的情况结果
        if n == 1:
            return a % b
            
        #recursion
        #a^n % b = (a^(n/2) * a^(n/2)) % b = ((a^(n/2) % b) * (a^(n/2) % b)) % b
        #这里的power = (a^(n/2) % b：由n=1的return结果recursion上来的.后续的result相当于在执行((a%b) * (a%b)) %b
        power = self.fastPower(a, b, n / 2)
        result = power * power % b
        
        #特判
        # 如果 n 是奇数，还需要多乘以一个 a，因为 n / 2 是整除
        if n % 2:
            result = result * a % b
        
        return result

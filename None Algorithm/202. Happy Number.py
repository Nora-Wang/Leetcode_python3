Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


思路:
数位分离+recursion
注意无限循环的情况,用self.record来记录出现过的temp

code:
class Solution(object):
    def __init__(self):
        self.record = set()
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #题目要求n为positive integer
        if n <= 0:
            return False
        
        #数位分离
        temp = 0
        while n:
            temp += (n % 10) ** 2
            n /= 10
        
        #题目要求的结果
        if temp == 1:
            return True
        
        #避免无限循环的情况
        if temp in self.record:
            return False
        
        #将当前temp加入self.record后,recursion
        self.record.add(temp)
        return self.isHappy(temp)
        

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.


code:
数位分离+recursion
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        
        temp = 0
        while num:
            temp += num % 10
            num /= 10
            
        return self.addDigits(temp)
        
        
        
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

发现规律,除了两个情况(num = 0时,返回0; num % 9 = 0时,返回9),其余情况都是返回num % 9
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        if num % 9:
            return num % 9
        else:
            return 9
        

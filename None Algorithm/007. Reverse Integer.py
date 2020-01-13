Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


code:
#数位分离
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        signal = 1
        if x < 0:
            signal = -1
        
        x = abs(x)
        result = 0
        while x:
            num = x % 10
            result = result * 10 + num
            x /= 10
        
        result *= signal
        
        #题目明确要求数据的取值范围[−231,  231 − 1]
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
        
        
#将数字转换为str,然后reverse
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        str_x = str(x)
        result = ''
        if str_x[0] == '-':
            result += '-'
            str_x = str_x[1:]
        
        #1.
        #for循环一个一个的倒着加进去
        #这里range的意思是:取值范围为len(str_x) - 1 ～ -1,步长为-1
        for i in range(len(str_x) - 1, -1, -1):
            result += str_x[i]
        
        #2.
        result = str_x[::-1]
        
        #3.
        result.reverse()
        
        result = int(result)
       
        if result < -2 ** 31 or result > 2 **31 - 1:
            return 0
        
        return result

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
             
             

特别多的corner case.....


code:
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #去除前后的空格
        str = str.strip(' ')
        
        #case 1: str为空
        if not str:
            return 0
        
        #case 2: 若开头不是数字/+/-时,则直接返回0
        if not str[0].isdigit() and (str[0] != '+' and str[0] != '-'):
            return 0
        
        #case 3: 若开头为+/-,则i+1
        i = 0
        if str[0] == '+' or str[0] == '-':
            i += 1
        
        #在范围内找到最大的数字
        while i < len(str) and str[i].isdigit():
            i += 1
        
        #case 4: '+'
        if i == 1 and (str[0] == '+' or str[0] == '-'):
            return 0
        
        #case 5: 数字不在[-2^31, 2^31 - 1]内
        #注意要int,str[:i] < -2**31永远都是true
        if int(str[:i]) < -2**31:
            return -2**31
        if int(str[:i]) > 2**31 - 1:
            return 2**31 - 1
            
        return int(str[:i])
        

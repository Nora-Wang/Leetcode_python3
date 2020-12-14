Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


思路:直接将int变为str,two pointer头尾扫一遍即可
code:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        start = 0
        end = len(x) - 1
        
        while start + 1 < end:
            if x[start] != x[end]:
                return False
            
            start += 1
            end -= 1
            
        return start == end or x[start] == x[end]
        
        
Follow up:
Coud you solve it without converting the integer to a string?

思路:数位分离 %10 /10,参考Integer to Roman
翻转数字比较相等即可,注意负数不是回文数  
code:
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #负数不是回文数
        if x < 0:
            return 0
        
        temp = x
        reverse = 0
        while temp:
            reverse = reverse * 10 + temp % 10
            temp /= 10
            
        return reverse == x

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


O(n*n)。对于每一个字符，以之作为中间元素往左右寻找。
注意
1.处理奇偶两种模式：aba, abba
2.奇偶两种情况都得算，然后做比较才能得出longest。因为对于caaaa，奇数的结果是aaa，偶数的结果是aaaa

code:
Version 0:
设置一个self.longest全局变量，直接在find_palindrom函数中对self.longest取最大值
class Solution(object):
    def __init__(self):
        self.longest = ''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        if len(s) == 2 and s[0] != s[1]:
            return s[0]
        
        for middle in range(len(s)):
            sub = self.find_palindrom(s, middle, middle + 1)
            sub = self.find_palindrom(s, middle, middle)
        return self.longest
    
    def find_palindrom(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        if len(self.longest) < right - left:
            self.longest = s[left:right]
                
                
Version 1:
最常规的方法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        longest = ''
        for middle in range(len(s)):
            sub = self.find_palindrom(s, middle, middle + 1)
            if len(longest) < len(sub):
                longest = sub
            sub = self.find_palindrom(s, middle, middle)
            if len(longest) < len(sub):
                longest = sub
        return longest
    
    def find_palindrom(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            left -= 1
            right += 1
        return s[left + 1:right]
                

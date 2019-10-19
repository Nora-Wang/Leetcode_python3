Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


O(n*n)。对于每一个字符，以之作为中间元素往左右寻找。
注意处理奇偶两种模式：
1. aba
2. abba


code:
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
                

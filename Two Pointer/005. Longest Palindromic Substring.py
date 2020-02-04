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
使用left和index记录当前longest Palindrome的起点index和整个的长度
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        left = 0
        index = 0
        count = 0
        
        for i in range(len(s)):
            index1, count1 = self.longest_palindrome(s, i, i)
            index2, count2 = self.longest_palindrome(s, i, i + 1)
            
            if count1 > count:
                count, index = count1, index1
            if count2 > count:
                count, index = count2, index2
        
        return s[index : index + count + 1]
    
    def longest_palindrome(self, s, left, right):
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count = right - left
            left -= 1
            right += 1
            
        return left + 1, count
            
              
                
Version 1:
使用string
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
                

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


code:

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return self.isPalindrome(s, start + 1, end) or self.isPalindrome(s, start, end - 1)
            else:
                start += 1
                end -= 1
        
        return True
            
            
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
                
            start += 1
            end -= 1
            
        return True

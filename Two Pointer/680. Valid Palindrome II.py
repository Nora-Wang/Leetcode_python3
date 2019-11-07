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


依然用相向双指针的方式从两头出发，两根指针设为 L 和 R。
如果 s[L] 和 s[R] 相同的话，L++, R--
如果 s[L] 和 s[R] 不同的话，停下来，此时可以证明，如果能够通过删除一个字符使得整个字符串变成回文串的话，那么一定要么是 s[L]，要么是 s[R]。
简单的来说，这个算法就是依然按照原来的算法走一遍，然后碰到不一样的字符的时候，从总选一个删除，如果删除之后的字符换可以是 Palindrome 那就可以，都不行的话，那就不行。

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

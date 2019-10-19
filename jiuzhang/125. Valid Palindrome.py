Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false



使用两根指针遍历整个字符串即可.
假定有指针i, j, 其中i是从前往后遍历, j是从后往前遍历.
当i在j左边时继续循环, 每一次将i右移到数字/字母上, j左移到数字/字母上,
比较二者对应的字符串内的字符是否相同, 不相同则原字符串不是回文串.
如果全部的比较都相同, 说明是回文串.

str.isalnum():检测字符串是否由字母和数字组成 = str.isalpha() and str.isdigit()
str.lower():转换字符串中所有大写字符为小写。



code:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
        

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


具体可参考44题,思路是一样的,只是判断标准变了一下

code:
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p, 0, 0, {})
    
    def helper(self, s, p, i, j, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == len(s):
            return self.is_match_p_rest(p[j:])
        
        if j == len(p):
            return False
        
        #当p的后面是'字母+*'的格式时,则分两种情况
        #1.s和p的当前字母一样,并且s后面的所有字母都符合条件
        #2.或者直接省略当前p的'字母+*',剩余字母都符合条件;eg:s = '', p = 'a*', 结果为True
        if j + 1 < len(p) and p[j + 1] == '*':
            matched = self.is_match_letter(s, p, i, j) and self.helper(s, p, i + 1, j, memo) or self.helper(s, p, i, j + 2,memo)
        else:
            matched = self.is_match_letter(s, p, i, j) and self.helper(s, p, i + 1, j + 1, memo)
            
        memo[(i,j)] = matched
        
        return matched
        
    def is_match_letter(self, s, p, i, j):
        return s[i] == p[j] or p[j] == '.'
    
    #判断p剩余部分是否符合条件:剩余部分一定要为'字母+*'格式(因为'字母+*'格式为看作空字符),因此剩余部分一定为偶数个
    def is_match_p_rest(self, p):
        #不为偶数直接返回False
        if len(p) % 2 != 0:
            return False
        
        #为偶数时,以步长为2的情况直接判断字母/*的后一个是不是*
        for i in range(0,len(p), 2):
            if p[i+1] != '*':
                return False
            
        return True

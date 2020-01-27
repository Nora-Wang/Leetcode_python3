Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


DP问题,match DP的可行性问题

时间复杂度为O(n*m)


code:
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match_helper(s, p, 0, 0, {})
    
    def is_match_helper(self, s, p, i, j, visited):
        #首先看有没有class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match_helper(s, p, 0, 0, {})
    
    def is_match_helper(self, s, p, i, j, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        #当s的所有字母都遍历完了后,只有当p剩余的字母都为*时,才为True
        if i == len(s):
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
            return True
        
        #因为前面分析过i == len(s)的情况了,因此这里if还有一个前提i<len(s),即s没有遍历完
        #当s没有遍历完,但j已经遍历结束时,结果一定为False
        if j == len(p):
            return False
        
        if p[j] != '*':
            #当前p不为*时,只有当前s和p的字母相同或p为?,并且s和p后面的所有字母都符合要求才为True
            matched = self.is_match_letter(s, p, i, j) and self.is_match_helper(s, p, i + 1, j + 1, memo)
        else:
            #当前p为*时,需要分支,因此两种情况只要有一种复合条件即可
            #如果pattern当前位是*，则需要判断string向后或者pattern向后是否匹配 
            #*可以代表一个或多个字母， *也可以代表空字符 
            matched = self.is_match_helper(s, p, i + 1, j, memo) or self.is_match_helper(s, p, i, j + 1, memo)
            
        #将当前结果记录
        memo[(i,j)] = matched
        
        return matched
   

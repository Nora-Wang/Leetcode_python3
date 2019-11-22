Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.



code:
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, {})
    
    def dfs(self, pattern, str, dict):
        #出口
        #这里同时处理了原始的pattern和str分别为空,以及同时为空的情况,在def wordPatternMatch中就不用单独加判断了
        if not pattern:
            return len(str) == 0
        
        #取pattern的第一个字母
        letter_pattern = pattern[0]
        #当前pattern的第一个字母在hash表中时
        if letter_pattern in dict:
            if not str.startswith(dict[letter_pattern]):
                return False
            return self.dfs(pattern[1:], str[len(dict[letter_pattern]):], dict)
        
        #当前pattern的第一个字母不在hash表中时
        for i in range(len(str)):
            word = str[:i + 1]
            if word in dict.values():
                continue
            dict[letter_pattern] = word
            if self.dfs(pattern[1:], str[i + 1:], dict):
                return True
            del dict[letter_pattern]
            
        return False

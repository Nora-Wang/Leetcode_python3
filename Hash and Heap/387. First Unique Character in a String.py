Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

    
    
#07/15/2020
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1
    
    
    
    
    
code:
#leetcode Version
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}
        
        for i in s:
            if i not in visited:
                visited[i] = 0
            visited[i] += 1
        
        for i in range(len(s)):
            if visited[s[i]] == 1:
                return i
        
        return -1
        
        
#lintcode Version
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        visited = {}
        
        for i in str:
            if i not in visited:
                visited[i] = 0
            visited[i] += 1
        
        for i in str:
            if visited[i] == 1:
                return i


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

code:
Version 1:用hash记录次数,按照s的顺序找到第一个次数为1的letter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = {}
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            
        result = len(s)
        for i in range(len(s)):
            if dict_s[s[i]] == 1:
                result = i
                break
            
        if result == len(s):
            return -1
        
        return result

Version 2:用hash记录letter的出现位置,取letter中只有一个index的最小值
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = []
            dict_s[s[i]].append(i)
            
        result = len(s)
        #这里可改为for letter in s,这样当dict_s[letter]为1时,直接取dict_s[letter]值即可;
        #重点是按照s的顺序循环的,因此第一个len(dict_s[letter])为1的letter,一定是firstUniqChar
        for letter in dict_s:
            if len(dict_s[letter]) > 1:
                continue
            
            result = min(dict_s[letter][0], result)
        
        if result == len(s):
            return -1
        
        return result
        
        
Version 2:最优
用hash记录letter的出现位置,一旦重复则赋值为len(s),最后取hash中values的最小值;若最小值为len(s),即连最后一个值len(s)-1都取不到,则返回-1
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dict_s = {}
        length = len(s)
        for i in range(length):
            if s[i] in dict_s:
                dict_s[s[i]] = length
            else:
                dict_s[s[i]] = i
            
        result = min(dict_s.values())
        if result == length:
            return -1
        return result


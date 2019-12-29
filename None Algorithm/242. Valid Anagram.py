Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.


code:
Version 1 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = 1
            else:
                mapping[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in mapping:
                return False
            mapping[t[i]] -= 1
        
        for item in mapping:
            if mapping[item] != 0:
                return False
            
        return True
        
        
        
Version 2 减少for循环的次数,将s和t的for循环合并到一起;缺点是需要牺牲空间,另加一个mapping
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #可不加,就是为了快点
        if s == t:
            return True
            
        if len(s) != len(t):
            return False
        
        mapping_s = {}
        mapping_t = {}
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = 1
            else:
                mapping_s[s[i]] += 1
        
            if t[i] not in mapping_t:
                mapping_t[t[i]] = 1
            else:
                mapping_t[t[i]] += 1
        
        for s_letter in mapping_s:
            if s_letter not in mapping_t or mapping_s[s_letter] != mapping_t[s_letter]:
                return False
            
        return True

Version 2.1 优化版,Version 2的代码太丑陋
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #可不加,就是为了快点
        if s == t:
            return True
            
        if len(s) != len(t):
            return False
        
        mapping_s = {}
        mapping_t = {}
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = 1
            mapping_s[s[i]] += 1
        
            if t[i] not in mapping_t:
                mapping_t[t[i]] = 1
            mapping_t[t[i]] += 1
        
        return mapping_s == mapping_t

Follow up 1:
要求O(n) time, O(1) extra space;用固定空间list来存储,代替hash
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #可不加,就是为了快点
        if s == t:
            return True
            
        if len(s) != len(t):
            return False
        
        #这个地方用两个list是为了避免:若s用+,t用-,最后需要for循环265次才能将整个count遍历判断全为0;
        #而用两个则O(1)的时间就可以判断两个list是否相等
        #设置为256是因为字母ASCII码最大为256
        s_count, t_count = [0] * 256, [0] * 256
        
        for i in range(len(s)):
            #ord函数返回值是字符对应的十进制整数
            s_count[ord(s[i])] += 1
            t_count[ord(t[i])] += 1
        
        return s_count == t_count



Follow up 2:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

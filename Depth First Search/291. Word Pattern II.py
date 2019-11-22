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
            #判断当前字符串是否是以letter_pattern在哈希表中值为开头的，如果不是，则返回F
            if not str.startswith(dict[letter_pattern]):
                return False
            #如果是继续递归找下一个pattern
            #注意pattern和str的取值范围的写法,str是要从该letter_pattern在hash表中对应的str的长度+1的位置开始取
            return self.dfs(pattern[1:], str[len(dict[letter_pattern]):], dict)
        
        #当前pattern的第一个字母不在hash表中时
        for i in range(len(str)):
            word = str[:i + 1]
            #如果当前字符串在字典的value中，需要跳过当前循环，继续向后找 
            #输入"ab" "aa"，如果不判断，哈希表中就是{a:a, b:a} 
            #此时返回的是True
            if word in dict.values():
                continue
            #制哈希表
            dict[letter_pattern] = word
            #向后递归
            if self.dfs(pattern[1:], str[i + 1:], dict):
                return True
            #镜像删除key
            del dict[letter_pattern]
            
        return False

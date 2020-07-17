Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


# 07/17/2020
# 记得问面试官：What should we return when needle is an empty string?
# time: O((n - m) * m), space: O(1), n = l_h, m = l_n
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l_h = len(haystack)
        l_n = len(needle)
        
        # 题目要求
        if not needle:
            return 0
        
        # 当needle不为空，但haystack为空； or needle的长度大于haystack -> -1
        if not haystack or l_h < l_n:
            return -1
        
        # 这里的取值范围需要多考虑一下，用一个例子算！
        for i in range(l_h - l_n + 1):
            if haystack[i:i + l_n] == needle:
                return i
        
        return -1
    
    
    
    
    
    
注意此题的corner case的判断不需要另写,因为在for循环里面就可以包括
思路:以len(needle)长度为标准,在haystack中寻找haystack[i:len(needle) + i]


code:
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:len(needle) + i]:
                return i
            
        return -1
            
            

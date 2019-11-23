Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


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
            
            

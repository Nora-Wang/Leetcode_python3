Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


从第一个开始比较，若不等则移向下一个(i);注意比较的范围是0～len(haystack) - len(needle)，但是range是取左不取右
当从i+0到i+len(needle)-1的值都相等时，则return i



code:
Version 0:
use while loop

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
        return -1
            
Version 1:
use for loop

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if haystack is None or needle is None:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                else:
                    if j == len(needle) - 1:
                        return i
        return -1
            

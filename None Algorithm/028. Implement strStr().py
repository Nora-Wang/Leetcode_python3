Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


# 07/17/2020
# 方法1
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
    
# 方法2: Rabin-Karp
# utilize an algorithm to compute a special num for curt sub_string, compare it with needle's num; utilize sliding window to compute the next sub_string
# time: O(n), space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_nee = len(needle)
        length_hay = len(haystack)
        
        # edge case: 比较长度
        if length_nee > length_hay:
            return -1
        
        # 担心后续的计算会stack overflow -> 利用取模来保证计算出的数据一定是在系统范围内的
        modulo = 2 ** 31
        # 避免后续代码冗杂重复 -> 提前定义好取int(c)的代码
        nee_to_int = lambda i:ord(needle[i]) - ord('a')
        hay_to_int = lambda i:ord(haystack[i]) - ord('a')
        
        num_nee = 0
        num_hay = 0
        for i in range(length_nee):
            num_nee = (num_nee * 26 + nee_to_int(i)) % modulo
            num_hay = (num_hay * 26 + hay_to_int(i)) % modulo
        
        # edge case: 第一组就相同
        if num_nee == num_hay:
            return 0
        
        # 得到最高位需要的数据: 26 ^ (length_nee - 1)
        highest_bit = 26 ** (length_nee - 1)
        
        # 利用sliding window的原理得到下一组的数据: (num_hay - 第i位的数据) * 26 + (i + length_nee的数据)
        for i in range(length_hay - length_nee):
            num_hay = ((num_hay - hay_to_int(i) * highest_bit) * 26 + hay_to_int(i + length_nee)) % modulo
            
            # 注意这里返回值是i + 1: 因为当前的num_hay是haystack[i+1:i+length_nee+1]的数据
            if num_hay == num_nee:
                return i + 1
        
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
            
            

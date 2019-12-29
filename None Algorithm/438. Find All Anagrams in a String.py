Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


code:
基本的想法:假设p串的长度为l,s串长度为n,那么就枚举出s中所有长度为l的子串，并用hash统计它们元素出现的个数
基本想法的时间复杂度:n个子串,每次统计子串中元素出现的个数O(l),每次和p对比元素出现次数是否一样O(256)/O(1),总体O( n * (l + 256/1)) = O(nl)
#######这样会超时
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        result = []
        for i in range(len(s) - len(p) + 1):
            if self.is_anagrams(s[i:i + len(p)], p):
                result.append(i)
                
        return result
    
    def is_anagrams(self, new_s, p):
        if new_s == p:
            return True
        
        count_s, count_p = {}, {}
        
        for i in range(len(p)):
            if new_s[i] not in count_s:
                count_s[new_s[i]] = 0
            count_s[new_s[i]] += 1
            
            if p[i] not in count_p:
                count_p[p[i]] = 0
            count_p[p[i]] += 1
            
        return count_s == count_p
            

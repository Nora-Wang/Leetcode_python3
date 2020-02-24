Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


sliding window + hash table
时间:O((s2-s1)*s1)

code:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        #先算好s1的情况
        hash_s1 = collections.Counter(s1)
        
        #sliding window,将每个substring与s1的hashtable做比较
        for i in range(len(s2) - len(s1) + 1):
            hash_s2 = collections.Counter(s2[i:i+len(s1)])
            
            if hash_s1 == hash_s2:
                return True
        
        return False

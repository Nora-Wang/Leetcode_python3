Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


# Map
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        mapping_s = {}
        mapping_t = {}
        
        for i in range(len(s)):
            if s[i] in mapping_s and mapping_s[s[i]] != t[i]:
                return False
            if t[i] in mapping_t and mapping_t[t[i]] != s[i]:
                return False
            
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
                
            s[i] = mapping_s[s[i]]

        #                 这部分是为了避免"badc","baba" case，即b、d都对应b，这不符合要求
        return s == t and len(mapping_s) == len(mapping_t)


# 2024/09/07 Map
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record_s2t = {}
        record_t2s = {}
        
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s not in record_s2t and char_t not in record_t2s:
                record_s2t[char_s] = char_t
                record_t2s[char_t] = char_s
                continue
            
            if char_s in record_s2t and record_s2t[char_s] != char_t:
                return False
            if char_t in record_t2s and record_t2s[char_t] != char_s:
                return False
                
        return True

# Array
# https://leetcode.com/problems/isomorphic-strings/discuss/57796/My-6-lines-solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_record, t_record = [0] * 256, [0] * 256
        
        for i in range(len(s)):
            if s_record[ord(s[i])] != t_record[ord(t[i])]:
                return False
            
            s_record[ord(s[i])] = i + 1
            t_record[ord(t[i])] = i + 1
        
        return True
            

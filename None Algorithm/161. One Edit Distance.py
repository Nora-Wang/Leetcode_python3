Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true
 

Constraints:

0 <= s.length <= 104
0 <= t.length <= 104
s and t consist of lower-case letters, upper-case letters and/or digits.

# time: O(n), space: O(1)

# personal version
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        
        if abs(l_s - l_t) >= 2:
            return False
        
        diff = 0
        index_s, index_t = 0, 0
        while index_s < l_s and index_t < l_t:
            # t need to insert one char, so that t == s
            if s[index_s] != t[index_t] and l_s > l_t:
                return s[index_s + 1:] == t[index_t:]
            # t need to delete one char, so that t == s
            elif s[index_s] != t[index_t] and l_t > l_s:
                return s[index_s:] == t[index_t + 1:]
            else:
                # l_t == l_s and s[index_s] != t[index_t] -> t need to replace only one char, so that t == s
                if s[index_s] != t[index_t]:
                    diff += 1
                    # more than one char need to be replaced
                    if diff == 2:
                        return False
                
                # s[index_s] == t[index_t] -> next comparison
                index_s += 1
                index_t += 1
                
        # case: 'ab', 'abcd' -> after the while loop, diff == 0, but index_s = index_t = 2 != l_t = 4
        diff += l_s - index_s + l_t - index_t
        return True if diff == 1 else False
        
        
# optimization
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        
        if abs(l_s - l_t) >= 2:
            return False
        
        diff = 0
        index_s, index_t = 0, 0
        for i in range(min(l_s, l_t)):
            if s[i] != t[i]:
                # t need to insert one char, so that t == s
                if l_s > l_t:
                    return s[i + 1:] == t[i:]
                # t need to delete one char, so that t == s
                elif l_t > l_s:
                    return s[i:] == t[i + 1:]
                # t need to replace only one char, so that t == s -> rest part are equal
                else:
                    return s[i + 1:] == t[i + 1:]
        
        # case: 'ab', 'abcd' -> after the while loop, every char is same, but index_s = index_t = 2 != l_t = 4
        return True if abs(l_s - l_t) == 1 else False
        

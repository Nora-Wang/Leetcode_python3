459. Repeated Substring Pattern
Easy

5987

473

Add to List

Share
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


Solution 1:
Rude solution

Time: O(n^2)
Space: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            
            subString = s[:i]
            if subString * (n // i) == s:
                return True
        
        return False


Solution 2:
Math solution

Time: O(n)
Space: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

        

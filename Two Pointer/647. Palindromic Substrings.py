Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.


背向双指针,参考leetcode 5


code:
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        count = 0
        
        for i in range(len(s)):
            count += self.count_palindromic(s, i, i)
            count += self.count_palindromic(s, i, i + 1)
        
        return count
    
    def count_palindromic(self, s, left, right):
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count

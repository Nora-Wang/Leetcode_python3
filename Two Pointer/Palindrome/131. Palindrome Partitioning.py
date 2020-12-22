Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


Version 1: Utilize 647. Palindromic Substrings
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []
        valid_palindrome_substring = set()
        for i in range(len(s)):
            self.palindrome_substring(s, i, i, valid_palindrome_substring)
            self.palindrome_substring(s, i, i + 1, valid_palindrome_substring)
        
        self.combination(s, 0, [], valid_palindrome_substring, res)
        
        return res
        
    def combination(self, s, index, temp, valid_palindrome_substring, res):
        if index == len(s):
            res.append(list(temp))
            return
        
        for i in range(index, len(s)):
            if s[index:i+1] not in valid_palindrome_substring:
                continue
            
            temp.append(s[index:i+1])
            self.combination(s, i+1, temp, valid_palindrome_substring, res)
            temp.pop()
        
        
    def palindrome_substring(self, s, left, right, valid_palindrome_substring):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            valid_palindrome_substring.add(s[left:right+1])
            left -= 1
            right += 1
            
            
            
Version 2: varify whether curt substring is palindrome
# Time complexity: O(n*(2^n))
# For a string with length n, there will be (n - 1) intervals between chars.
# For every interval, we can cut it or not cut it, so there will be 2^(n - 1) ways to partition the string.
# For every partition way, we need to check if it is palindrome, which is O(n).
# So the time complexity is O(n*(2^n))
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []
        self.dfs(s, 0, [], res)
        
        return res
    
    def dfs(self, s, index, temp, res):
        if index == len(s):
            res.append(list(temp))
            return
        
        for i in range(index, len(s)):
            if self.is_palindrome(s, index, i):
                temp.append(s[index:i+1])
                self.dfs(s, i+1, temp, res)
                temp.pop()
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

       
       
# Version 3: Version 2 + memo
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        self.memo = {}
        self.helper(s, 0, [], res)
        
        return res
    
    def helper(self, s, index, temp, res):
        if index == len(s):
            res.append(list(temp))
            return
        
        for i in range(index, len(s)):
            if self.is_palindrome(s, index, i):
                temp.append(s[index:i+1])
                self.helper(s, i+1, temp, res)
                temp.pop()
    
    def is_palindrome(self, s, start, end):
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        
        while start < end:
            if s[start] != s[end]:
                self.memo[(start, end)] = False
                return False
            start += 1
            end -= 1
            
        self.memo[(start, end)] = True
        return True

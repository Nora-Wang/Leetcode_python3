Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

********************************************************************** 
Solution 1:
# DFS
# time: O(n^2), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict))
    
    def dfs(self, s, wordDict):
        if not s:
            return False
        
        if s in wordDict:
            return True
        
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict):
                return True

        return False
        
**********************************************************************        
# optimization: memo + DFS
# time: O(n^2), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict), {})
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return False
        
        if s in wordDict:
            memo[s] = True
            return True
        
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict, memo):
                memo[s] = True
                return True
        
        memo[s] = False
        return False
      
********************************************************************** 
# time: O(1. m < n : O(m * n); 2. m > n : O(n ^ 2)), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        
        m = len(max(wordDict, key=len))
        return self.dfs(s, set(wordDict), m, {})
    
    def dfs(self, s, wordDict, m, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return False
        
        if s in wordDict:
            memo[s] = True
            return True
        
        for i in range(1, min(m, len(s)) + 1):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict, m, memo):
                memo[s] = True
                return True
        
        memo[s] = False
        return False

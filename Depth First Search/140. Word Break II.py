Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]


# DFS
# time: O(n^2), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, set(wordDict))
    
    def dfs(self, s, wordDict):
        res = []
        
        if not s:
            return []
        
        if s in wordDict:
            res.append(s)
        
        for i in range(1, len(s)):
            if s[:i] in wordDict:
                left = s[:i]
                wordlist = self.dfs(s[i:], wordDict)
                
                for right in wordlist:
                    res.append(left + ' ' + right)
        
        return res
        
        
        
        
        
# memo + DFS
# time: O(n^2), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, set(wordDict), {})
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        res = []
        
        if not s:
            return []
        
        if s in wordDict:
            res.append(s)
        
        for i in range(1, len(s)):
            if s[:i] in wordDict:
                left = s[:i]
                wordlist = self.dfs(s[i:], wordDict, memo)
                
                for right in wordlist:
                    res.append(left + ' ' + right)
        
        memo[s] = res
        return res

      
# memo + DFS
# time: O(n * min(n * m)), space: O(n), n = len(s), m = wordDict中最长单词的长度（the lenght of longest word in wordDict）
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 后续需要取到对wordDict进行max，因此需要判断一下
        if not wordDict:
            return []
        
        # m = wordDict中最长单词的长度
        m = len(max(wordDict, key=len))
        return self.dfs(s, set(wordDict), {}, m)
    
    def dfs(self, s, wordDict, memo, m):
        if s in memo:
            return memo[s]
        
        res = []
        
        if not s:
            return []
        
        if s in wordDict:
            res.append(s)
        
        # 注意这里的取值范围，因为后续s[:i],i取不到，所以都得+1
        for i in range(1, min(m, len(s)) + 1):
            if s[:i] in wordDict:
                left = s[:i]
                
                wordlist = self.dfs(s[i:], wordDict, memo, m)
                
                for right in wordlist:
                    res.append(left + ' ' + right)
        
        memo[s] = res
        return res
      

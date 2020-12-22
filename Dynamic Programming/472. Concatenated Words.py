Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 6 * 105

# Version 2: DP





# Version 1: optimal DFS
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) <= 1:
            return []
        
        words = set(words)
        
        res = []
        for word in words:
            if len(word) == 0:
                continue
            if self.helper(words, word, 0):
                res.append(word)
        
        return res
    
    def helper(self, words, word, start):
        if start == len(word):
            return True
        
        for end in range(len(word), start, -1):
            if word[start:end] not in words or word[start:end] == word:
                continue
                
            if self.helper(words, word, end):
                return True
            
        return False


# Version 0: 自己写的DFS
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        lengths = []
        for word in words:
            lengths.append(len(word))
        
        res = []
        for word in words:
            if not word:
                continue
            if self.helper(words, word, 0, lengths):
                res.append(word)
        
        return res
    
    def helper(self, words, word, start, lengths):
        if start == len(word):
            return True
        
        for length in lengths:
            if length >= len(word) or start + length > len(word):
                continue
            
            if word[start:start + length] not in words:
                continue
                
            if self.helper(words, word, start + length, lengths):
                return True
            
        return False

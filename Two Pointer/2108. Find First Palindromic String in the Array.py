Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.

# Reverse String
# m = longest word length, n = len(words)
# Time O(m), Space O(n)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if not len(words):
            return ''
        
        for word in words:
            if word == word[::-1]:
                return word
            
        return ''

# Two pointer
# m = longest word length, n = len(words)
# Time O(m), Space O(n)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if not len(words):
            return ''
        
        for word in words:
            if self.isPalindromic(word):
                return word
            
        return ''
    
    def isPalindromic(self, word):
        start, end = 0, len(word) - 1
        
        # aa
        while start < end:
            if word[start] != word[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

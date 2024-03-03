Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


# Split Array
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.split(' ')

        for word in list_s[::-1]:
            if word.isalnum():
                return len(word)
        
        return -1

# Two Pointer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        fast, slow = 0, 0
        word = ''
        while fast < len(s):
            if s[slow] == ' ':
                slow += 1
                fast += 1
                continue
            
            while fast < len(s) and s[fast] != ' ':
                fast += 1
            
            word = s[slow:fast]
            slow = fast
        
        return len(word)

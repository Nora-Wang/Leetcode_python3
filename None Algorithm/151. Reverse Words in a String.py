Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


# Version 1
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
   
# Version 2








'''
clarification
input: string, None?, ''?, only lowercase letters and space?
output: string

1. utilize Python split function
list = string.split()
split -> reversed -> ' '.join
time: O(n), space: O(n)

2. two pointer
find the valid sub_string = s[left:right], no space
while left < len(s):
    1. s[left] == ' ' -> continue
    2. s[left] != ' '
        right = left
        while right < len(s) and s[right] != ' ':
            right += 1
        append s[left:right] into res
        left = right
    
    reverse res, use join function to get the string res

time: O(n), space: O(n)

3. 
'''

# version 1
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

# version 2
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        
        res = []
        left = 0
        
        while left < len(s):
            if s[left] == ' ':
                left += 1
                continue
            
            right = left
            while right < len(s) and s[right] != ' ':
                right += 1
            
            res.append(s[left:right])
            left = right
        
        return ' '.join(reversed(res))

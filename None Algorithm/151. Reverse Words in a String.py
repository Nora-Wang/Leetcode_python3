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
# split之后将单词顺序reverse
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
   
# Version 2
# 不用split，用while loop找到每个单词，最后将单词顺序reverse
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []

        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            
            start = index
            while index < len(s) and s[index].isalnum():
                index += 1
            
            res.append(s[start:index])
        
        return ' '.join(reversed(res))

       
 # Version 3
 # 不用split，用while loop找到每个单词
 # 先将整个string reverse，然后再将每个单词reverse
 class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]

        res = []
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            
            start = index
            while index < len(s) and s[index].isalnum():
                index += 1
            res.append(s[start:index][::-1])
        
        return ' '.join(res)

# Version 4
# 不用split，用while loop找到每个单词
# 用deque.appendleft将每个单词加入deque的头部（相当于将单词顺序reverse的操作）
class Solution:
    def reverseWords(self, s: str) -> str:
        deque = collections.deque()

        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            
            start = index
            while index < len(s) and s[index].isalnum():
                index += 1
            
            deque.appendleft(s[start:index])

        return ' '.join(deque)






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

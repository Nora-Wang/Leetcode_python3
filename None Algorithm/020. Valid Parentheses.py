Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Data Structure题
题目考的就是对stack的理解与运用

code:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            #注意这里要用elif(逻辑)
            if c == '{':
                stack.append('}')
            elif c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            
            elif not stack or c != stack.pop():
                return False
            
        return not stack

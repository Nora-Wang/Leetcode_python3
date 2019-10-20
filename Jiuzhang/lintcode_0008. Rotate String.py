Given a string(Given in the way of char array) and an offset, rotate the string by offset in place. (rotate from left to right).

Example
Example 1:

Input: str="abcdefg", offset = 3
Output: str = "efgabcd"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

Example 5:

Input: str="abcdefg", offset = 10
Output: str = "efgabcd"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".



三步翻转法：先翻两个小的，再翻大的
example1:
1.0, len(s) - offset - 1:  dcbaefg
2.len(s) - offset, len(s) - 1:  dcbagfe
3.0, len(s) - 1:   efgabcd

注意边界的取值

code:
Version 0:
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s:
            return s
        offset %= len(s)
        if offset == 0:
            return s
        
        self.revers_string(s, 0, len(s) - offset - 1)
        self.revers_string(s, len(s) - offset, len(s) - 1)
        self.revers_string(s, 0, len(s) - 1)
        return s
    
    def revers_string(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        

Version 1:
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s:
            return
            
        offset %= len(s)
        
        if offset == 0:
            return
###注意s的写法！！
        # str_left = s[:len(s) - offset]
        # str_right = s[len(s) - offset:]
        # s[:] = str_right + str_left
        s[:] = s[len(s) - offset:] + s[:len(s) - offset]
        
    
        

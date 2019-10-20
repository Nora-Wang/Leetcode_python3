Given a string(Given in the way of char array), a right offset and a left offset, rotate the string by offset in place.(left offest represents the offset of a string to the left,right offest represents the offset of a string to the right,the total offset is calculated from the left offset and the right offset,split two strings at the total offset and swap positions)。

Example
Example 1:

Input：str ="abcdefg", left = 3, right = 1
Output："cdefgab"
Explanation：The left offset is 3, the right offset is 1, and the total offset is left 2. Therefore, the original string moves to the left and becomes "cdefg"+ "ab".
Example 2:

Input：str="abcdefg", left = 0, right = 0
Output："abcdefg"
Explanation：The left offset is 0, the right offset is 0, and the total offset is 0. So the string remains unchanged.
Example 3:

Input：str = "abcdefg",left = 1, right = 2
Output："gabcdef"
Explanation：The left offset is 1, the right offset is 2, and the total offset is right 1. Therefore, the original string moves to the left and becomes "g" + "abcdef".




code:
class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        if not str:
            return str
        offsite = left - right
        
        if offsite == 0:
            return str
            
        elif offsite > 0:
            self.revers_string(str, 0, offsite - 1)
            self.revers_string(str, offsite, len(str) - 1)
            
        else:
            self.revers_string(str, 0, len(str) + offsite - 1)
            self.revers_string(str, len(str) + offsite, len(str) - 1)
            
        self.revers_string(str, 0, len(str) - 1)
            
    def revers_string(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1
            

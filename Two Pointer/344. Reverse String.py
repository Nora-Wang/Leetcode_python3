Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

# time: O(n), space: O(1)
 
# 1. Python function
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        return
      
      
      
# 2. interation
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return
       
# 3.  recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        
        self.helper(s, 0, len(s) - 1)
        
        return
    
    def helper(self, s, left, right):
        if left >= right:
            return
        
        s[left], s[right] = s[right], s[left]
        
        self.helper(s, left + 1, right - 1)
 
 
 


code:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        
        start, end = 0, len(s) - 1
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        

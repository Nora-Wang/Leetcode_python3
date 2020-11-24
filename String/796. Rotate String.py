We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

# Solution 1
# time: O(n^2), space: O(n)
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        # edge case: A = B = ''
        if not A and not B:
            return True
        
        # 用list比string省空间
        A_list = list(A)
        B_list = list(B)
        
        for i in range(len(A_list)):
            if A_list[i:] + A_list[:i] == B_list:
                return True
        
        return False
        
        
# Solution 2
真大神的写法，细思极恐
def rotateString(self, A, B):        
    return len(A) == len(B) and B in A + A

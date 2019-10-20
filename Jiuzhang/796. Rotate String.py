We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false


code:
#将A挨个翻转，若其中一个能与B相同，则为True
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if not A and not B:
            return True
        
        for i in range(len(A)):
            new = A[i:] + A[:i]
            if new == B:
                return True
        return False
        
        
        
真大神的写法，细思极恐
def rotateString(self, A, B):        
    return len(A) == len(B) and B in A + A

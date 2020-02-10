Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


code:
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return True
        
        start, end = 1, num
        
        while start + 1 < end:
            #这里取整
            mid = (start + end) // 2
            
            if mid ** 2 == num:
                return True
            
            if mid ** 2 < num:
                start = mid
            else:
                end = mid
        
        #只要有满足条件的,就是true
        if end ** 2 == num or start ** 2 == num:
            return True
        
        return False

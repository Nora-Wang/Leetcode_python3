Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.


主要是堆的运用
code:
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        
        heap = [1]
        visited = set([1])
        
        for _ in range(n):
            ugly_num = heapq.heappop(heap)
            
            for positive_num in [2,3,5]:
                new_ugly = ugly_num * positive_num
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return ugly_num

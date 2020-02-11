Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Example

Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
Challenge

O(n log Len), where Len is the longest length of the wood.

Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.


注意题目的意思是equal or more than k pieces,而这些pieces必须要有相同长度,求最长长度

code:
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L:
            return 0
        
        #这里end取最大
        start, end = 1, max(L)
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.get_count(mid, L) < k:
                end = mid
            else:
                start = mid
        
        #equal or more than k pieces,且取最长
        if self.get_count(end, L) >= k:
            return end
        
        if self.get_count(start, L) >= k:
            return start
        
        return 0
    
    def get_count(self, mid, L):
        count = 0
        
        for wood in L:
            count += wood // mid
        
        return count

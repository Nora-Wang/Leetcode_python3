Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

'''
1. min_heap
push all elements in min_heap, pop k elements
2. max_heap
keep len(max_heap) == k, pop one element

3. binary search
'''


# max_heap
# time: O(nlogk), space: O(n)
from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not len(matrix) or not len(matrix[0]):
            return None
        
        max_heap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(max_heap, -matrix[i][j])
                
                if len(max_heap) > k:
                    heappop(max_heap)
                
        return -heappop(max_heap)


# min_heap
# time: O(nlogn), space: O(n)
from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not len(matrix) or not len(matrix[0]):
            return None
        
        min_heap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(min_heap, matrix[i][j])
        
        for _ in range(k - 1):
            heappop(min_heap)
        
        return heappop(min_heap)

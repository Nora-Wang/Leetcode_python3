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


一开始要clarify k与n大小的关系



merge k sorted array思路

code:
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not len(matrix) or not len(matrix[0]):
            return None
        
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        for _ in range(k):
            res, x, y = heapq.heappop(heap)
            
            #这里要判断一下y的取值
            if y + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
            
        return res

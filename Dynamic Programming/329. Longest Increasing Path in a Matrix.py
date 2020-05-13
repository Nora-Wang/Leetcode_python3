Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


code:
#DFS + memo





#DFS (Time Limit Exceeded)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        
        self.res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, 0, -float('inf'))
        
        return self.res
    
    def dfs(self, matrix, x, y, count, prev):
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            return
        
        if matrix[x][y] <= prev:
            return
        
        if count == self.res:
            self.res = count + 1
        
        for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
            x_ = x + direct[0]
            y_ = y + direct[1]
            
            self.dfs(matrix, x_, y_, count + 1, matrix[x][y])

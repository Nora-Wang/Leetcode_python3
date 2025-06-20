Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# 2025/06/20
# DFS - TLE
  class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0

        self.res = float('inf')
        record = {(0,0):grid[0][0]}
        self.dfs(grid, 0, 0, grid[0][0], record)

        return self.res

    def dfs(self, grid, i, j, temp, record):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            self.res = min(self.res, temp)
            return
        
        for d_i, d_j in [(0,1), (1,0)]:
            i_, j_ = i + d_i, j + d_j

            if i_ < len(grid) and j_ < len(grid[0]):
                if (i_,j_) in record and record[(i_,j_)] < temp + grid[i_][j_]:
                    continue
                
                record[(i_,j_)] = temp + grid[i_][j_]
                self.dfs(grid, i_, j_, temp + grid[i_][j_], record)
        
        return

  
06/02/2020
'''
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

dp[i][j] means row = i, col = j, the min path sum for curt position

time: O(n * m), space: O(1)
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i and j:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                else:
                    if i:
                        grid[i][j] += grid[i - 1][j]
                    if j:
                        grid[i][j] += grid[i][j - 1]

        return grid[-1][-1]
        
  

使用DP是因为这道题也是向一个方向(右下)运动的
动规方程式dp[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

code:
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        dp = grid
        
        #初始化第一列的数据
        for i in range(1,len(grid)):
            dp[i][0] += dp[i - 1][0]
        
        #初始化第一行的数据
        for j in range(1,len(grid[0])):
            dp[0][j] += dp[0][j - 1]
        
        #向右下角取最小path和
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
        #右下角的和即为最小和
        return dp[-1][-1]

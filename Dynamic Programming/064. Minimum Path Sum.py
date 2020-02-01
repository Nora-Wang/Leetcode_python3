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

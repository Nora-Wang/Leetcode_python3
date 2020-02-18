A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28



【确认条件】
（1）求解法总数。
（2）机器人只能往下或者往右走。
（3）确认哪边是m，哪边是n。

【解题思路】
（1）确定状态：dp[i][j]表示到达此处的方案总数。
（2）转移方程：要想到达dp[i][j]，得先到达dp[i - 1][j]或者dp[i][j - 1]。所以 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
（3）初始状态和边界情况：到达最上面一行或最左侧一列只有一种方案：即沿着边走。所以 i = 0 或者 j = 0 时dp初始化为1。
（4）计算顺序：从左上方到右下方。

【复杂度】
时间复杂度：O(m * n)
空间复杂度：O(n)


code:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        #第一个赋值为1
        dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                #当是左上角的值时,略过,否则后续会out of index
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
    
    
递归解法:超时
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    #递归出口
        if m < 0 or n < 0:
            return 0
        
        if m == 1 and n == 1:
            return 1
        
        up = self.uniquePaths(m-1, n)
        left = self.uniquePaths(m,n-1)
        
        return up + left

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?


坐标型DP + 滚动数组

code:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (rowIndex + 1), [1] * (rowIndex + 1)]
        
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i % 2][j] = dp[i % 2 - 1][j] + dp[i % 2 - 1][j-1]

        return dp[rowIndex % 2]
        
        

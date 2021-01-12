Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.


'''
1. DFS 穷举所有的case，一旦Alex赢了 -> return True
           ''
        /       \
 A     5(0)    5(3)
     /       \
 L  3(1)     5(3)
   /   \
A 4(2)  5(3)
  /        \
L 5(3)    4(2)
每次是2个选择，深度len(piles)
dfs(piles, left, right, sum_A, sum_L, turn=1)
if turn % 2: A choose max(piles[left], piles[right]) -> go to next recursion round
else: L choose max(piles[left], piles[right]) -> go to next recursion round


2. DP
left = i, right = j
dp[i][i] = [pile[i], pile[i]]
dp[i][j][0]: piles[i:j+1] has max stones for A
dp[i][j][1]: piles[i:j+1] has max stones for L

dp[i][i] = [pile[i], 0]

for distance in range(1, n):
   for i in range(n - distance):
      j = i + distance
      dp[i][j][0] = max(dp[i + 1][j][1] + piles[i], dp[i][j - 1][1] + piles[j])
      if A choosed i -> dp[i][j][1] = dp[i + 1][j][0]
      if A choosed j -> dp[i][j][1] = dp[i][j - 1][0]

if dp[0][-1][0] > dp[0][-1][1] -> True
else -> False

'''

# 3D DP
# time: O(n^2), space: O(n^2)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[0,0] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = [piles[i], 0]

        for distance in range(1, n):
            for i in range(n - distance):
                j = i + distance
                if dp[i + 1][j][1] + piles[i] > dp[i][j - 1][1] + piles[j]:
                    dp[i][j][0] = dp[i + 1][j][1] + piles[i]
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = dp[i][j - 1][1] + piles[j]
                    dp[i][j][1] = dp[i][j - 1][0]

        return dp[0][-1][0] > dp[0][-1][1]

# 2D optimal
# time: O(n^2), space: O(n^2)
class Solution:
   def stoneGame(self, piles: List[int]) -> bool:
      n = len(piles)
      dp = [[0 for _ in range(n)] for _ in range(n)]
      for i in range(n):
         dp[i][i] = piles[i]

      for distance in range(1, n):
         for i in range(n - distance):
            dp[i][i + distance] = max(dp[i - 1][i + distance] + piles[i], dp[i][i + distance - 1] + piles[i + distance - 1])
      
      return dp[0][-1] > sum(piles) - dp[0][-1]
      
# 1D
# time: O(n), space: O(n)
class Solution:
   def stoneGame(self, piles: List[int]) -> bool:
      n = len(piles)
      dp = list(piles)

      for distance in range(1, n):
         for i in range(n - distance):
            j = i + distance
            dp[i] = max(dp[i + 1] + piles[i], dp[j - 1] + piles[j])
      
      return dp[0] > sum(piles) - dp[0]
      

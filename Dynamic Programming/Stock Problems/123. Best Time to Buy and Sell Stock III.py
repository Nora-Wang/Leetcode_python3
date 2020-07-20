Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''
1. define:
dp[i][k][choose]
i = day, [0 len(price)]
k = 2
choose = [0, 1], 0 = no stock, 1 = have stock

2. function
原始方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

3. end case
if i - 1 = -1 -> i = 0:
dp[i][k][0] = 0
dp[i][k][1] = -float('inf')
dp[i][k-1][0] = 0
dp[i][k-1][1] = -float('inf')

time: O(n), space: O(n)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = len(prices)
        max_k = 2
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(l)]
        dp[0][max_k][0], dp[0][max_k][1] = 0, -float('inf')
        dp[0][max_k-1][0], dp[0][max_k-1][1] = -float('inf'), -float('inf')
        
        for i in range(1, l):
            for k in range(max_k, 0, -1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                
        return dp[-1][max_k][0]
        
        
        
# 因为k = 2，数据很小，可以直接写
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = len(prices)
        dp = [[[0, 0] for _ in range(2 + 1)] for _ in range(l)]
        
        for i in range(l):
            if i - 1 == -1:
                dp[i][2][0], dp[i][2][1] = 0, -float('inf')
                dp[i][1][0], dp[i][1][1] = 0, -float('inf')
                continue
                    
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
        
        return dp[-1][2][0]

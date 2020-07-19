Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]


'''
1. define:
dp[i][k][choose]
i = day, [0 len(price)]
k = 0 ～ float('inf')
choose = [0, 1], 0 = no stock, 1 = have stack
2. function:
简化版
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
3. end case:
i - 1 = -1 -> i = 0
dp[i][0] = 0
dp[i][1] = -prices[0]（用上面的公式算一下）

i - 2 = -1 -> i = 1
dp[i][0] = max(0, -prices[0] + prices[1])
dp[i][1] = max(-prices[0], -prices[1])

time: O(n), space: O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        
        dp = [[None, None] for _ in range(len(prices))]
        # initail
        dp[0][0], dp[0][1] = 0, -prices[0]
        dp[1][0], dp[1][1] = max(0, -prices[0] + prices[1]), max(-prices[0], -prices[1])
        
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            
        return dp[-1][0]
        
        
        
# space简化版
# time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        
        dp_i_0, dp_i_1 = 0, -prices[0]
        temp = dp_i_0
        dp_prev_0 = 0
        
        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_prev_0 - prices[i])
            
            dp_prev_0 = temp
            temp = dp_i_0
            
        return dp_i_0

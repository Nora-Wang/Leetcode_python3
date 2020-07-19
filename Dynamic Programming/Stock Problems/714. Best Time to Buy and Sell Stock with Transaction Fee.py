Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


'''
1. define:
dp[i][k][choose]
i = day, [0 len(price)]
k = 0 ～ float('inf')
choose = [0, 1], 0 = no stock, 1 = have stack
2. function:
简化版
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
3. end case:
i - 1 = -1
dp[i][0] = 0
dp[i][1] = -prices[i] - fee（用上面的公式算一下）
time: O(n), space: O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        dp = [[None, None] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                continue
                
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        
        return dp[-1][0]
        
        
        
# space简化版
# time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        dp_i_0, dp_i_1 = 0, -prices[0] - fee
        
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        
        return dp_i_0

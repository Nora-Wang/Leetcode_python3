Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
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
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4



# 07/19/2020
'''
1. define:
dp[i][k][choose]
i = day, [0 len(price)]
k = 1
choose = [0, 1], 0 = no stock, 1 = have stack

2. function:
简化版
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

3. end case:
i - 1 = -1
dp[i][0] = 0
dp[i][1] = -prices[i]（用上面的公式算一下）

time: O(n), space: O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[None, None] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
                
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        return dp[-1][0]
        
        
# space简化版
# time: O(n), space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp_i_0, dp_i_1 = 0, -prices[0]
        # 因为在求dp_i_1时还需要用到dp_i_0被改变前的数据，因此用temp记录一下
        temp = dp_i_0
        
        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
            
            temp = dp_i_0
        
        return dp_i_0
        
        

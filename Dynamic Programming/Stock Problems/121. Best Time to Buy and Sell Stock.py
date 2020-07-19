Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


# 07/19/2020

# DP
'''
1. define:
dp[i][k][choose]
i = day, [0 len(price)]
k = 1
choose = [0, 1], 0 = no stock, 1 = have stack

2. function
原始方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

简化版：
dp[i][0] = max(dp[i - 1][1] + price[i], dp[i - 1][0])
dp[i][1] = max(dp[i - 1][1], -price[i])

3. end case
if i - 1 = -1:
dp[i][0] = 0
dp[i][1] = -price[i] ——> dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i]) = max(-float('inf'), 0 - prices[i]) 

time: O(n), space: O(n)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = len(prices)
        dp = [[None, None] for _ in range(l)]
        
        for i in range(l):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
                
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        
        return dp[-1][0]
                
# DP release space version
# time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        
        for i in range(1, l):
            # 用之前的dp_i_1和dp_i_0来进行计算，得到当前的dp_i_1和dp_i_0
            dp_i_0 = max(dp_i_1 + prices[i], dp_i_0)
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0                
  
  
  
  
  
  
  
# 直接写的：O(1) space
'''
curt, min_r, max_r, profit
1. curt < min_r
renew profit = max(curt_profit), min_r = curt, max_r = curt
2. min_r <= curt < max_r
renew profit, max_r = curt
3. curt >= max_r
renew profit, max_r = curt

time: O(n), space: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_r = max_r = prices[0]
        profit = 0
        
        for curt in prices:
            if curt < min_r:
                min_r = curt
            max_r = curt
            profit = max(max_r - min_r, profit)
        
        return profit


  
  
  
  
  
code:
#Array解法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        curt_min = prices[0]
        distance = 0
        result = 0
        index = 0
        for i in range(1, len(prices)):
            if prices[i] < curt_min:
                curt_min = prices[i]
                distance = 0
                continue
                
            if prices[i] - curt_min > distance:
                index = i
                distance = prices[i] - curt_min
                result = max(result, distance)

        return result

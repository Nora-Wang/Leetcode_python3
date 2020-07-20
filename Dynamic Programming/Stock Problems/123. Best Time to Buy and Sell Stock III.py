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



1. define:
dp[k][i] for every transaction find the max profit
K = 2
i = [0, len(prices)]

2. function
dp[k][i] = max(rest, sell)
dp[k][i] = max(dp[k][i - 1], prices[i] + buy in 0~i-1)
buy in 0~i-1 = max(dp[k-1][j] - prices[j]), j in range(0, i)

3. end case:
k = 0 or i = 0 -> profit = 0
dp[0][i]是因为没有操作transaction，所以为0
dp[k][0]是因为如果price array长度为1的话，如[3]，因为当天不能多次交易，所以最大profit是0

# time: O(k * n * n), space: O(n * k), k = 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        K = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(2 + 1)] 
        
        for k in range(1, K + 1):
            for i in range(1, len(prices)):
                max_buy = -float('inf')
                for j in range(0, i):
                    max_buy = max(max_buy, dp[k - 1][j] - prices[j])
                    
                dp[k][i] = max(dp[k][i - 1], max_buy + prices[i])
        
        return dp[K][-1]
    
# Optimization
为了得到max_buy，每次都是O(n)的时间去进行计算，但其实每次比的都一样，所以直接用max_buy记住当前的最大即可，这样就少一层循环
# time: O(k * n), space: O(n * k), k = 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        K = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(2 + 1)] 
        
        for k in range(1, K + 1):
            max_buy = -float('inf') 
            for i in range(1, len(prices)):
                max_buy = max(max_buy, dp[k - 1][i - 1] - prices[i - 1])
                dp[k][i] = max(dp[k][i - 1], max_buy + prices[i])
        
        return dp[K][-1]    


  
  
  
  
  
  
  
# 套路
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

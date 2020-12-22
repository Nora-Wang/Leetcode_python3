You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4


# Version 1: DFS TLE
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        coins.sort(reverse=True)
        self.res = float('inf')
        
        self.helper(coins, 0, 0, amount)
        
        return self.res if self.res != float('inf') else -1
    
    def helper(self, coins, index, count, amount):
        if index == len(coins):
            return
        
        if amount == 0:
            self.res = min(self.res, count)
            return
        
        # prune
        if amount < 0 or count >= self.res:
            return
        
        self.helper(coins, index, count + 1, amount - coins[index])
        self.helper(coins, index + 1, count + 1, amount - coins[index])
        self.helper(coins, index + 1, count, amount)
